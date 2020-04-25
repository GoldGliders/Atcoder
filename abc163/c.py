from collections import Counter
n = int(input())
a = Counter(map(int, input().split()))

for n in range(1, n+1):
    try:
        print(a[n])
    except:
        print(0)
