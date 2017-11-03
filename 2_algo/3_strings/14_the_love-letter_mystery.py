T = int(input())
for _ in range(T):
    s = input()
    slen = len(s)
    cnt = 0
    for i in range(slen//2):
        if s[i] != s[slen-i-1]:
            cnt += abs(ord(s[i]) - ord(s[slen-i-1]))
    print(cnt)