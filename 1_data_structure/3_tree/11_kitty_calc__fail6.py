
treeMap = {}
n, q = map(int, input().split(' '))

a, b = map(int, input().split(' '))
if not a in treeMap.keys():
    treeMap[a] = {}
if not b in treeMap.keys():
    treeMap[b] = {}
treeMap[a][b] = 1
treeMap[b][a] = 1

for _ in range(n-2):
    a, b = map(int, input().split(' '))
    
    flagA = False
    if not a in treeMap.keys():
        treeMap[a] = {}
        flagA = True
    else:
        treeMap[b] = {}

    treeMap[a][b], treeMap[b][a] = 1, 1

    if flagA:
        newX, oldX = a, b
    else:
        newX, oldX = b, a
    
    for key in treeMap.keys():
        if key != oldX and key != newX:
            treeMap[key][newX] = treeMap[newX][key] = \
            treeMap[key][oldX] + treeMap[oldX][newX]

# Calculate
for _ in range(q):
    k = int(input())
    node = list(map(int, input().split(' ')))
    
    s = 0
    for i in range(k-1):
        for j in range(i+1, k):
            s += (node[i] * node[j] * treeMap[node[i]][node[j]])
    
    kitty_cal = s % (10**9 + 7)
    print(kitty_cal)