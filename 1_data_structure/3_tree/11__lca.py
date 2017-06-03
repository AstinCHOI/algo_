
# https://www.acmicpc.net/problem/11438
# http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220820773477
import math

n = int(input())

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


for _ in range(n-1):
	u, v = map(int, input().split(' '))
	adj[u].append(v)
	adj[v].append(u)

	
depth[1] = 0
makeDFSTree(1)
 
for i in range(MAX):
	for j in range(1, n+1):
		if parent[i][j] != -1:
			parent[i+1][j] = parent[i][parent[i][j]]

q = int(input())
for _ in range(q):
	u, v = map(int, input().split(' '))

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

	print(u)

## Input
# 15
# 1 2
# 1 3
# 2 4
# 3 7
# 6 2
# 3 8
# 4 9
# 2 5
# 5 11
# 7 13
# 10 4
# 11 15
# 12 5
# 14 7
# 6
# 6 11
# 10 9
# 2 6
# 7 6
# 8 13
# 8 15

## Output
# 2
# 4
# 2
# 1
# 3
# 1