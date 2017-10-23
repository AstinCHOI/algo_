# final
T = int(input())

for _ in range(T):
    N = int(input())
    grid = []
    for i in range(N):
        grid.append(sorted(input()))

    flag = True
    for i in range(1, N):
        for j in range(1, N):
            if not ((ord(grid[i-1][j-1]) <= ord(grid[i-1][j])) and \
                (ord(grid[j-1][i-1]) <= ord(grid[j][i-1]))):
                flag = False
                break
        if not flag:
            break

    if flag:
        print('YES')
    else:
        print('NO')

# 2nd
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     grid = []
#     for i in range(N):
#         grid.append(sorted(input()))

#     rows = []
#     cols = []
#     flag = True
#     for i in range(1, N):
#         row = []
#         col = []
#         for j in range(1, N):
#             row.append(ord(grid[i-1][j]) - ord(grid[i-1][j-1]))
#             col.append(ord(grid[j][i-1]) - ord(grid[j-1][i-1]))
#         rows.append(row)
#         cols.append(col)

#         if i >= 2 and ((rows[0] != rows[i-1]) or (cols[0] != cols[i-1])):
#             flag = False
#             break
#     if flag:
#         print('YES')
#     else:
#         print('NO')


# 1st
# T = int(input())
# N = int(input())

# for _ in range(T):
#     first = sorted(input())
#     pre = ord(first[0])
#     std = []
#     for a in first[1:]:
#         std.append(ord(a)-pre)
#         pre = ord(a)

#     flag = True
#     for _ in range(N-1):
#         others = sorted(input())
#         pre = ord(others[0])
#         for i in range(1, N):
#             if pre + std[i-1] != ord(others[i]):
#                 flag = False
#                 break
#             else:
#                 pre = ord(others[i])
#         if not flag:
#             break
#     if flag:
#         print('YES')
#     else:
#         print('NO')
    
    