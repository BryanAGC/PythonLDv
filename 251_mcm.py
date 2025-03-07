import math

def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print(mcm(4, 5))
