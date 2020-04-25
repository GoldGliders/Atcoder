mod = 10**9 + 7
n, a, b = map(int, input().split())

ans = pow(2, n, mod)

def C(n, k):
    x, y = 1, 1
    for i in range(k):
        x = x *(n - i) % mod
        y = y *(i+1) % mod

    return (x * pow(y, mod-2, mod)) % mod

print((ans - C(n, a) - C(n, b) - 1) % mod)

