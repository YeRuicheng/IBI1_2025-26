import matplotlib.pyplot as plt
import numpy as np

# Define population data and calculate percentage change
population_data = {
    'UK': {'2020': 66.7, '2024': 69.2},
    'China': {'2020': 1426, '2024': 1410},
    'Italy': {'2020': 59.4, '2024': 58.9},
    'Brazil': {'2020': 208.6, '2024': 212.0},
    'USA': {'2020': 331.6, '2024': 340.1}
}

# Calculate percentage change for each country
percent_changes = {}
for country, data in population_data.items():
    pop_2020 = data['2020']
    pop_2024 = data['2024']
    pct_change = ((pop_2024 - pop_2020) / pop_2020) * 100
    percent_changes[country] = pct_change

# Print percentage change for each country
print("Percentage population change (2020-2024):")
for country, change in percent_changes.items():
    print(f"{country}: {change:.2f}%")

# Sort changes and identify extremes

# Sort by percentage change (descending: largest increase to largest decrease)
sorted_changes = sorted(percent_changes.items(), key=lambda x: x[1], reverse=True)

print("\nPopulation changes sorted from largest increase to largest decrease:")
for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")

# Identify largest increase and decrease
largest_increase_country = sorted_changes[0][0]
largest_increase_value = sorted_changes[0][1]
largest_decrease_country = sorted_changes[-1][0]
largest_decrease_value = sorted_changes[-1][1]

print(f"\nThe country with the largest population increase is {largest_increase_country} ({largest_increase_value:.2f}%).")
print(f"The country with the largest population decrease is {largest_decrease_country} ({largest_decrease_value:.2f}%).")

# Create labeled bar chart
countries = list(percent_changes.keys())
changes = list(percent_changes.values())

plt.figure(figsize=(9, 5))
bars = plt.bar(countries, changes, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height > 0 else -0.3),
             f'{height:.2f}%', ha='center', va='bottom' if height > 0 else 'top')

plt.xlabel('Country', fontsize=12)
plt.ylabel('Percentage Change in Population (%)', fontsize=12)
plt.title('Population Percentage Change (2020-2024) by Country', fontsize=14, pad=15)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)  # Add zero line
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()