# Import required libraries
import os
import matplotlib.pyplot as plt
import pandas as pd

# Load the DALYs dataset from CSV file into a DataFrame
os.chdir("C:/Users/叶睿城/Desktop")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Display first 10 rows, selecting only Year and DALYs columns
print("=== First 10 rows (Year & DALYs) ===")
first_10 = dalys_data.iloc[0:10, [2, 3]]
print(first_10)

# Use Boolean indexing to filter all rows for Zimbabwe
dalys_zimbabwe = dalys_data.loc[dalys_data['Entity'] == 'Zimbabwe', 'Year']
print("\n=== All Years recorded for Zimbabwe ===")
print(dalys_zimbabwe)

# Find and print the first and last year for Zimbabwe
first_year_zim = dalys_zimbabwe.min()
last_year_zim = dalys_zimbabwe.max()
print("\nFirst year for Zimbabwe:", first_year_zim)
print("Last year for Zimbabwe:", last_year_zim)

# Filter data for the year 2019 (Entity & DALYs)
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]

# Find the index of the maximum DALYs value in the recent_data DataFrame, using .idxmax()
max_index = recent_data['DALYs'].idxmax()

# Retrieve the country name corresponding to the maximum DALYs value
max_country = recent_data.loc[max_index, 'Entity']

# Find the country of the minimum DALYs value in the recent_data DataFrame (similar to finding the maximum)
min_index = recent_data['DALYs'].idxmin()
min_country = recent_data.loc[min_index, 'Entity']

print("\n=== 2019 DALYs Extremes ===")
print("Country with MAX DALYs:", max_country)
print("Country with MIN DALYs:", min_country)

# Filter the original DataFrame to get all rows for the country with the maximum DALYs value
country_max = dalys_data[dalys_data['Entity'] == max_country]

# Plot the DALYs values over time for the country with the maximum DALYs value
plt.figure(figsize=(10, 5))
plt.plot(country_max['Year'], country_max['DALYs'], 'b+', label = max_country)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Over Time for ' + max_country)
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Extra Questions: 
# 1. How has the relationship between DALYs in China and the UK changed over time?
# 2. Are they becoming more similar or less similar?

# Extract data for China and UK
china = dalys_data.loc[dalys_data['Entity'] == 'China', ['Year', 'DALYs']]
uk = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom', ['Year', 'DALYs']]

# Plot both countries on the same graph
plt.figure(figsize=(10, 5))
plt.plot(china['Year'], china['DALYs'], 'b-', label='China')
plt.plot(uk['Year'], uk['DALYs'], 'r-', label='UK')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Trend: China vs UK (1990–2019)')
plt.legend()
plt.xticks(rotation=-90)
plt.show()

# Calculate the difference (absolute value) between China and UK DALYs over time (compare 1990 and 2019)
# Merge two DataFrames by Year using .merge(), with suffixes to differentiate the DALYs columns
merged = china.merge(uk, on='Year', suffixes=('_China', '_UK'))
merged['Difference'] = abs(merged['DALYs_China'] - merged['DALYs_UK'])
gap_1990 = merged['Difference'].iloc[0]
gap_2019 = merged['Difference'].iloc[-1]

# If statement to judge similarity
print("\n=== Similarity Analysis: China vs UK ===")
print("Difference between China and UK DALYs in 1990:", merged['Difference'].iloc[0])
print("Difference between China and UK DALYs in 2019:", merged['Difference'].iloc[-1])
if gap_2019 < gap_1990:
    print("Gap decreased → China and UK are becoming MORE SIMILAR.")
elif gap_2019 > gap_1990:
    print("Gap increased → China and UK are becoming LESS SIMILAR.")
else:
    print("Gap stayed the same → No change in similarity.")