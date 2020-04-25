a = [list(map(int, input().split())) for _ in range(3)]
a = a[0] + a[1] + a[2]
c = [
        a[0:3], a[3:6], a[6:9], a[::3], a[1::3], a[2::3],
        [a[0], a[4], a[8]], [a[2], a[4], a[6]]
    ]
n = int(input())
b = [int(input()) for _ in range(n)]


same = set(a) & set(b)

for d in c:
    cnt = 0
    for n in same:
        if n in d:
            cnt += 1
    if cnt == 3:
        print("Yes")
        exit()
else:
    print("No")
