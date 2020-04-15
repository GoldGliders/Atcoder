n, m = map(int, input().split())
ans = 0

# even + even
ans += n * (n-1) / 2
# odd + odd
ans += m * (m-1) / 2
print(round(ans))
