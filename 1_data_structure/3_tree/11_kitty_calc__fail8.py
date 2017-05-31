
# with Lowest Common Ancestor
import math

treeMap = {}

MAX = int(math.ceil(math.log(2*10**5, 2)))
adj = [ [] for _ in range(n+1) ]
parent = [ [ -1 for _ in range(n+1) ] for _ in range(MAX) ]
depth = [ -1 for _ in range(n+1) ]

def makeDFSTree(curr):
    for next in adj[curr]:
        if depth[next] == -1:
            parent[0][next] = curr
            depth[next] = depth[curr] + 1
            makeDFSTree(next)

# Lowest Common Ancestor
def getLCA(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    
    j=0
    while diff != 0:
        if diff % 2 != 0:
            u = parent[j][u]
        j+=1
        diff = int(diff / 2)

    if u != v:
        for k in range(MAX-1, -1, -1):
            if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]

        u = parent[0][u]

    return u

def getDistance(u, v):
    lca = getLCA(u, v)
    # dist = ( depth[u] - depth[lca] ) + ( depth[v] - depth[lca] )
    return depth[u] + depth[v] - (depth[lca] * 2)

if __name__ == "__main__":
    n, q = map(int, input().split(' '))
    for _ in range(n-1):
        u, v = map(int, input().split(' '))
        adj[u].append(v)
        adj[v].append(u)

    depth[1] = 0
    makeDFSTree(1)

    # Make Parent Table for DP(Dynamic Programming)
    for i in range(MAX):
        for j in range(1, n+1):
            if parent[i][j] != -1:
                parent[i+1][j] = parent[i][parent[i][j]]

    # Calculate
    for _ in range(q):
        k = int(input())
        node = list(map(int, input().split(' ')))
        
        s = 0
        for i in range(k-1):
            for j in range(i+1, k):
                s += (node[i] * node[j] * getDistance(node[i], node[j]))
        
        kitty_cal = s % (10**9 + 7)
        print(kitty_cal)