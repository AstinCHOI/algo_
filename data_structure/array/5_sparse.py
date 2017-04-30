N = int(raw_input())
arr = []
for _ in xrange(N):
    arr.append(raw_input())

M = int(raw_input())
for _ in xrange(M):
    line = raw_input()
    num = 0
    for j in xrange(N):
        num = num + (line == arr[j])
    print(num)

## Input
# 4
# aba
# baba
# aba
# xzxb
# 3
# aba
# xzxb
# ab

## Output
# 2
# 1
# 0