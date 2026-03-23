import matplotlib.pyplot as plt
import numpy as np

# Initialize heart rate data and calculate basic statistics
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rates)
mean_hr = np.mean(heart_rates)

# Display total patients and average heart rate
print(f"There are {num_patients} patients in the dataset, with a mean heart rate of {mean_hr:.2f} bpm.")

# Classify heart rates into categories
low = 0
normal = 0
high = 0

# Iterate through each heart rate value
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1

# Display counts for each category
print(f"\nNumber of patients in each category:")
print(f"Low (<60 bpm): {low}")
print(f"Normal (60-120 bpm): {normal}")
print(f"High (>120 bpm): {high}")

# Determine the largest category
categories = {'Low': low, 'Normal': normal, 'High': high}
largest_category = max(categories, key=categories.get)
print(f"\nThe {largest_category} heart rate category contains the largest number of patients.")

# Create a labeled pie chart
labels = ['Low (<60 bpm)', 'Normal (60-120 bpm)', 'High (>120 bpm)']
sizes = [low, normal, high]
colors = ['#FF9999', '#66B2FF', '#99FF99']
explode = (0, 0.1, 0)

# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('Distribution of Resting Heart Rate Categories', fontsize=14, pad=15)
plt.axis('equal')
plt.tight_layout()
plt.show()