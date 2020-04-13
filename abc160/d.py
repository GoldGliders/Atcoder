n, x, y = map(int, input().split())

dst = [0 for _ in range(n-1)]
for i in range(1, n+1):
    for j in range(i+1, n+1):
        dst[min(abs(i-j), abs(x-i)+1+abs(y-j))-1] += 1

for d in dst:
    print(d)
