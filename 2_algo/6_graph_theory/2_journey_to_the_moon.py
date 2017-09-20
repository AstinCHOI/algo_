N, P = tuple(map(int, input().strip().split(' ')))

sets = [{i} for i in range(N)]
arr = [i for i in range(N)] # sets[arr[i]] contains i <= pointer

for i in range(P):
    a, b = tuple(map(int, input().strip().split(' ')))
    if a not in sets[arr[b]]:
        #union the sets
        u = sets[arr[a]] | sets[arr[b]]
        sets[a] = u #store the union at sets[a]
        for j in u: #pointers to a
            if j!=a:
                sets[j]=set()
            arr[j]=a # <-- A move of got

total = 0
non_singles = 0
for i in range(N):
    #print(sets[arr[i]], sets[i])
    L = len(sets[i])
    if L>1: #non-single set with length L
        non_singles += L
        #add pairs with first person in the subset
        total += L*(N-L)

#singles = N - non_singles
#add pairs with first person in the set of singles 
total = total + (N-non_singles)*(N-1)

#remove double counting
total = total//2
print(total)


#####################
# Okay, but timeout for 1 case (using DFS-Depth First Search)

N, P = map(int, input().split(' '))

visited = [False] * N
ast = [[] for _ in range(N)]
    
for _ in range(P):
    A, B = map(int, input().split(' '))
    ast[A].append(B)
    ast[B].append(A)

def all_visited():
    for i in range(N):
        if visited[i] == False:
            return i
    return -1

# print(ast)
group = []
solo = 0
node = all_visited()
while node != -1:
    stack = [node]
    count = 1
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            for w in ast[u]:
                if not visited[w] and w not in stack:
                    stack.append(w)
                    count += 1
    
    if count > 1:
        group.append(count)
    else:
        solo += 1
    
    node = all_visited()
    
group.append(solo)
g = len(group)
result = 0
for i in range(g):
    for j in range(i+1, g):
        result += (group[i] * group[j])

print(result + (solo*(solo-1)//2))

## 1st try
# N, P = map(int, input().split(' '))

# ast = {}
# mark = [0] * N
# for i in range(N):
#     ast[i] = set()
    
# for _ in range(P):
#     A, B = map(int, input().split(' '))
#     ast[A].add(B)
#     ast[B].add(A)

# print(ast)

# same = []
# solo = 0
# marked = [False] * N
# for i in range(N):
#     res = 1
#     if not marked[i]:
#         if len(ast[i]) != 0:
#             for j in ast[i]:
#                 res += 1
#                 marked[j] = True
#             same.append(res)
#             marked[i] = True
#         else:
#             solo += 1

# t = 0
# s = 1
# if len(same) > 1:
#     for i in same:
#         s *= i
#         t += (i * solo)
#     tot = s + t
# else:
#     tot = same[0] * solo

# print(tot + (solo*(solo-1)//2))


## 2nd try
# N, P = map(int, input().split(' '))

# ast = []
# mark = [0] * N
# solo = [1] * N
    
# for _ in range(P):
#     A, B = map(int, input().split(' '))
#     g = {A, B}
#     solo[A] = solo[B] = 0
    
#     flag = True
#     for i in range(len(ast)):
#         if ast[i].intersection(g):
#             ast[i] = ast[i].union(g)
#             flag = False
#             break
            
#     if flag:
#         ast.append(g)

# dmarked = []
# if i in range(len(ast)):
#     for j in range(len(ast)):
#         if i != j and ast[i].intersection(ast[j]):
#             ast[i] = ast[i].union(ast[j])
#             dmarked.append(j)

# for i in dmarked:
#     del ast[i]

# ast_len = list(map(len, ast))
# m = 1
# ms = 0
# s = sum(solo)
# for j in ast_len:
#     m *= j
#     ms += (j * s)

# print(m + ms + (s*(s-1)//2))