
# Timeout

import sys
sys.setrecursionlimit((2**31)-1)

tree_dict = {}
tree_map = {}
def dist(a, b, visited, way, distance, up):
    if a == b:
        tree_map[way[0]][b] = tree_map[b][way[0]] = distance
        return distance
    elif b in tree_map[a].keys():
        if way[0] == a:
            return tree_map[a][b]

    for node in tree_dict[a]:
        if node not in visited:
            visited.append(node)
            way.append(node)
            return dist(node, b, visited, way, distance+1, up)
    
    # print(way)
    tree_map[way[0]][way[-1]] = tree_map[way[-1]][way[0]] = distance
    way.remove(way[-1])
    return dist(visited[up-1], b, visited, way, distance-1, up-1)

n, q = map(int, input().split(' '))
for _ in range(n-1):
    a, b = map(int, input().split(' '))

    if a not in tree_dict.keys():
        tree_dict[a] = [b]
        tree_map[a] = {}
    else:
        tree_dict[a].append(b)

    if b not in tree_dict.keys():
        tree_dict[b] = [a]
        tree_map[b] = {}
    else:
        tree_dict[b].append(a)

# Calculate
for _ in range(q):
    k = int(input())
    node = list(map(int, input().split(' ')))
    
    s = 0
    for i in range(k):
        for j in range(i+1, k):
            visited = [node[i]]
            way = [node[i]]
            s += (node[i] * node[j] * dist(node[i], node[j], visited, way, 0, -1))
    
    kitty_cal = s % (10**9 + 7)
    print(kitty_cal)