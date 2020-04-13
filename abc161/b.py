N, M = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
t = sum(A)
if t/(4*M) <= A[M-1]:
    print("Yes")
else:
    print("No")
