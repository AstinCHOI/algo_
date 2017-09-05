n = int(input())
point = list(map(int, input().split(' ')))
m = int(input())
alice = list(map(int, input().split(' ')))

rank = [0] * n
pre = 0
for i in range(n):
    if pre == point[i]:
        rank[i] = rank[i-1]
    else:
        rank[i] += rank[i-1] + 1
    pre = point[i]


for ap in alice:
    mid, low = 0, 0
    high = n-1
   
    while(low <= high):
        mid = int((low + high) / 2)
        if ap < point[mid]:
            low = mid+1
        elif ap > point[mid]: s
            high = mid-1
        else:
            break
            
    mid = int((low + high) / 2)
    if ap < point[mid]:
        print(rank[mid] + 1)
    elif ap > point[mid]:
        if rank[mid] != 1:
            print(rank[mid] - 1)
        else:
            print(1)
    else:
        print(rank[mid])
