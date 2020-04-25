n, m = map(int, input().split())

ans = [-1]*n
a = 0
for i in range(m):
    s, c = map(int, input().split())
    if s == 1 and c == 0 and n != 1:
        a = -1
    elif ans[s-1] not in [-1, c]:
        a = -1
    else:
        ans[s-1] = c

if a == -1:
    print(a)
else:
    b = ""
    if ans[0] == -1 and n != 1:
        ans[0] = 1
    for x in ans:
        if x == -1:
            b += "0"
        else:
            b += str(x)
    print(b)
