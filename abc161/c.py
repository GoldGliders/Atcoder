n, k = map(int, input().split())

n1 = n % k
n2 = k - n1
print(n1 if n1 < n2 else n2)
