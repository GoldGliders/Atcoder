n, a, b = map(int, input().split())
c = a + b
ans = 0
ans += a * (n // c)
if n % c >= a:
    ans += a
else:
    ans += n % c
print(ans)
