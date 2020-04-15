import collections

n = int(input())
A = list(map(int, input().split()))
B = collections.Counter(A)

s = 0
for k, i in B.items():
    s += i*(i-1) // 2
for a in A:
    print(s-(B[a]-1))
