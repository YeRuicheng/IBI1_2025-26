# infection.py
# Calculate the number of days to infect all 91 students in IBI1 class

# Set total number of students in the class
total_students = 91

# Initial number of infected students and daily growth rate
initial_infected = 5
growth_rate = 0.4  # 40% growth per day

# Initialize day counter and current infected count
days = 1
current_infected = initial_infected

# Print the first day's infection status
print(f"Day {days}: {current_infected} infected students")

# Loop until all students are infected
while current_infected < total_students:
    # Calculate new number of infected students for the next day
    current_infected = current_infected * (1 + growth_rate)
    # Increase day count
    days += 1
    # Print infection status for the current day
    print(f"Day {days}: {current_infected} infected students")

# Print the final result
print(f"\nTotal days needed to infect all {total_students} students: {days} days")
