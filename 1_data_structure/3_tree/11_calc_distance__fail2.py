
# Timeout

import sys
sys.setrecursionlimit(10000)

tree_dict = {}
tree_map = {}
def dist(a, b, visited, way, distance, up, s):
    if not b:
        return s
    elif a in b:
        s += visited[0] * a * distance
        b.remove(a)

    for node in tree_dict[a]:
        if node not in visited:
            visited.append(node)
            # way.append(node)
            return dist(node, b, visited, way, distance+1, up, s)

    # print(visited)
    # print(way)
    # way.remove(way[-1])
    return dist(visited[up-1], b, visited, way, distance-1, up-1, s)


n, q = map(int, input().split(' '))

# Make Queue
for _ in range(n-1):
    a, b = map(int, input().split(' '))


    if a not in tree_dict.keys():
        tree_dict[a] = [b]
    else:
        tree_dict[a].append(b)

    if b not in tree_dict.keys():
        tree_dict[b] = [a]
    else:
        tree_dict[b].append(a)


# Calculate
for _ in range(q):
    k = int(input())
    node = list(map(int, input().split(' ')))
    
    s = 0
    for i in range(k):
        visited = [node[i]]
        way = [node[i]]
        # s += (node[i] * node[j] * dist(node[i], node[j], visited, 0, -1))
        s += dist(node[i], node[i+1:], visited, way, 0, -1, 0)
    kitty_cal = s % (10**9 + 7)
    print(kitty_cal)