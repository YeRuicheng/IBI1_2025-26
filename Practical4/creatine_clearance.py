# This program calculates Creatinine Clearance (CrCl) using age, weight, creatine concentration, and gender
# It validates all input values and uses different formulas for male and female

# Get user input for age and convert it to an integer
a = int(input("Enter age:"))

# Check if age is 100 or older
if a >= 100:
    print("Age must be between 0 and 100 years.")
    exit()

# Get user input for weight and convert it to an integer
w = int(input("Enter weight(kg):"))
# Check if weight is outside the valid range (20 - 80 kg)
if w <= 20 or w >= 80:
    print("Weight must be between 20 and 80 kg.")
    exit()

# Get user input for creatine concentration and convert it to an integer
Cr = int(input("Enter creatine concentration(µmol/l):"))
# Check if creatine level is outside the valid range (0 - 100)
if Cr <= 0 or Cr >= 100:
    print("Creatine concentration must be between 0 and 100 µmol/l.")
    exit()

# Get user input for gender (M/F)
gender = str(input("Enter gender (M/F):"))
if gender == "M":
    CrCl = ((140 - a) * w) / (72 * Cr)
elif gender == "F":
    CrCl = ((140 - a) * w * 0.85) / (72 * Cr)

# Print the final CrCl result
print("CrCl is " + str(CrCl))