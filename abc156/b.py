n, k = map(int, input().split())

ans = 0
while True:
    ans += 1
    if pow(k, ans)-1 >= n:
        print(ans)
        break

