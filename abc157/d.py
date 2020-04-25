n, m, k = map(int, input().split())
friend = [[] for _ in range(n+1)]
block = [[] for _ in range(n+1)]
btw = [0]*n
cand = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

for _ in range(k):
    c, d = map(int, input().split())
    block[c].append(d)
    block[d].append(c)

for i in range(1, n):
    if i+1 in friend[i]:
        btw[i] = 1

for i in range(1, n):
    for j in range(i+1, n):
        if btw[i] == 1 or all(btw[i:j]):
            if i not in friend[j] and i not in block[j]:
                cand[i] += 1
                cand[j] += 1
print(cand)
