n, k = map(int, input().split())
arr = [0] * 1000000

m = 1000000
M = 0
li = list(map(int, input().split()))
for i in li:
    arr[i] = 1
    if i < m:
        m = i
    if i > M:
        M = i

i = m
cnt = 0        

while i <= M:
    if arr[i] == 0:
        i += 1
        continue
        
    pt = i + k
    while not arr[pt]: pt-=1
    i = (pt + k + 1) 
    cnt+=1

print(cnt)