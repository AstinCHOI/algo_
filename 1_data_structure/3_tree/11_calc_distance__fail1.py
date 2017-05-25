
# Timeout
import sys
sys.setrecursionlimit(1500)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.nodes = []


tree_dict = {}
def dist(a, b, visited, distance, up):
    if a == b:
        return distance
    for node in tree_dict[a].nodes:
        if node not in visited:
            visited.append(node)
            return dist(node, b, visited, distance+1, up)
#    print(visited)
    return dist(visited[up-1], b, visited, distance-1, up-1)

n, q = map(int, input().split(' '))

for _ in range(n-1):
    a, b = map(int, input().split(' '))
    if a not in tree_dict.keys():
        tree_dict[a] = Node(a)

    if b not in tree_dict.keys():
        tree_dict[b] = Node(b)

    tree_dict[a].nodes.append(b)
    tree_dict[b].nodes.append(a)

# Calculate
for _ in range(q):
    k = int(input())
    node = list(map(int, input().split(' ')))
    
    s = 0
    for i in range(k):
        for j in range(i+1, k):
            visited = [node[i]]
#            print("{}*{}*{}".format(node[i], node[j], dist(node[i], node[j], visited, 0, -1)))
            s += (node[i] * node[j] * dist(node[i], node[j], visited, 0, -1))
    
    kitty_cal = s % (10**9 + 7)
    print(kitty_cal)