k = int(input())
n = list(map(str, range(10)))

i = 0
while len(n) < k+1:
    i += 1
    # -1, 0, 1
    for j in range(-1, 2):
        # 一の位
        m = n[i][-1]
        if j == -1 and m == "0":
            continue
        if j == 1 and m == "9":
            break
        p = n[i] + n[int(m)+j]
        n.append(p)


print(n[k])
