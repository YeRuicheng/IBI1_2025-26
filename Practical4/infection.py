#initial student(a):5
#growth rate(r):0.4
#day(d)

a = 5
r = 0.4
d = 0
while a < 91:
    d = d + 1
    a = a + r*a
print("It takes",d,"days for the infection to reach",a, "people.")