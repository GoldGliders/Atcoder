k, n = map(int, input().split())
a = list(map(int, input().split()))

b = []
b.append(a[0]+(k-a[-1]))
for i in range(1, n):
    b.append(a[i] - a[i-1])
b.sort()
print(sum(b[:-1]))
