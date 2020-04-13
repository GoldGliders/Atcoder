import math
k = int(input())
t = 0
# a = b = c
for x in range(1, k+1):
    t += x
# a = b != c
for a in range(1, k+1):
    for b in range(a+1, k+1):
        t += 6*math.gcd(a, b)
# a != b != c
for a in range(1, k+1):
    for b in range(a+1, k+1):
        for c in range(b+1, k+1):
            d = math.gcd(a, b)
            t += 6*math.gcd(d, c)
print(t)
