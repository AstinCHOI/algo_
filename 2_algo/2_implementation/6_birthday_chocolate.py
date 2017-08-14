n = int(input())
ch = list(map(int, input().split(' ')))
d, m = map(int, input().split(' '))

cnt = 0
for i in range(n):
    if (n - m + i) >= 0 and sum(ch[i:i+m]) == d:
        cnt = cnt + 1

print(cnt)