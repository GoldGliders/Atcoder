n = int(input())
s = input()
t = s.count("R")*s.count("G")*s.count("B")
for i in range(n):
    for j in range(i+1, n):
        k = 2*j - i
        if k < n and s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            t -= 1

print(t)
