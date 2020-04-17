from math import floor
a, b = map(int, input().split())

for x in range(1, 10**5):
    if floor(x*0.08) == a and floor(x*0.1) == b:
        print(x)
        exit()
print(-1)
