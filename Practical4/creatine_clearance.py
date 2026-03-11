#age(a), weight(w)
a = int(input("Enter age:"))
if a >= 100:
    print("Age must be between 0 and 100 years.")
    exit()
w = int(input("Enter weight(kg):"))
if w <= 20 or w >= 80:
    print("Weight must be between 20 and 80 kg.")
    exit()
Cr = int(input("Enter creatine concentration(µmol/l):"))
if Cr <= 0 or Cr >= 100:
    print("Creatine concentration must be between 0 and 100 µmol/l.")
    exit()
gender = str(input("Enter gender (M/F):"))
if gender == "M":
    CrCl = ((140 - a) * w) / (72 * Cr)
elif gender == "F":
    CrCl = ((140 - a) * w * 0.85) / (72 * Cr)
print("CrCl is " + str(CrCl))