t = int(input())
for _ in range(t):
    st = input()
    cnt = 0
    pre = st[0]
    for i in range(1, len(st)):
        if pre == st[i]:
            cnt += 1
        else:
            pre = st[i]
    print(cnt)