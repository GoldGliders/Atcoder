MOD = 10**9 + 7
n, k = map(int, input().split())
ans = 0
for i in range(k, n+2):
    mn = (0+(i-1))*i*0.5
    mx = (n+(n-(i-1)))*i*0.5
    ans += mx - mn + 1

print(int(ans%MOD))
