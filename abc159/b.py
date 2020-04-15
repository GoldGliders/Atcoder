s = input()
n = len(s)
t = s[:(n-1)//2]
u = s[(n+3)//2-1:]

if s == s[::-1]:
    if t == t[::-1]:
        if u == u[::-1]:
            print("Yes")
            exit()
print("No")
