n = int(input())
bs = input()

# 1 from discussion
print((n - len(bs.replace('010', '')))//3)

# 2
# cnt = 0
# i = 0
# while i < n:
#     if bs[i] == '0' and i+2 < n and bs[i+1] == '1' and bs[i+2] == '0':
#         cnt += 1
#         i += 3
#     else:
#         i += 1
# print(cnt)