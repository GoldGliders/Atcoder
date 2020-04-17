s = input()
q = int(input())
d = True
head = []
tail = []
for i in range(q):
    t, *u= input().split()
    if t == "1":
        d = not d
    else:
        f, c = u[0], u[1]
        if d:
            if f == "1":
                head.append(c)
            else:
                tail.append(c)
        else:
            if f == "1":
                tail.append(c)
            else:
                head.append(c)
s = "".join(head)[::-1] + s + "".join(tail)
print(s if d else s[::-1])
