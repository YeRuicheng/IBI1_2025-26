a = 5.08*(10**6)
b = 5.33*(10**6)
c = 5.55*(10**6)
d = b-a
e = c-b
if d > e:
    print("2004-2014 is larger. The population growth is decelerating.")
else:
    print("2014-2025 is larger. The population growth is accelerating.")
# D is larger. The population growth is decelerating.

X = True
Y = False
W = X or Y
# Truth table for W = X or Y:
# X     | Y     | W
# True  | True  | True
# True  | False | True
# False | True  | True
# False | False | False