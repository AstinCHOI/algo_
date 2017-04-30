## O(MN)
# N, M = map(int, raw_input().split(' '))
# arr = [0] * N

# a, b, k = map(int, raw_input().split(' '))
# arr[a-1:b] = ([k]*(b-a+1))

# for j in xrange(M-1):
#     a, b, k = map(int, raw_input().split(' '))

#     pre = arr[a-1]
#     prek = arr[a-1] + k
#     for z in xrange(a-1, b):
#         if pre == arr[z]:
#             arr[z] = prek
#         else:
#             pre = arr[z]
#             arr[z] = prek = arr[z] + k

# #    arr[a-1:b] = map((lambda x: x + k), arr[a-1:b])

# print(max(arr))

## O(NlogN)
N, M = map(int, raw_input().split(' '))
arr = [0] * (N+1)
for i in xrange(M):
    a, b, k = map(int, raw_input().split(' '))
    arr[a-1] += k
    arr[b] += (k * -1)

prem = 0
m = -1
for j in xrange(N):
    prem += arr[j]

    if m < prem:
        m = prem

print(m)

## Input
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100

## Output
# 200


## https://codereview.stackexchange.com/questions/95755/algorithmic-crush-problem-hitting-timeout-errors
#          #   1.......................N...N+1
# 5 3      #   0     0     0     0     0     0
# 1 2 100  # 100     0  -100     0     0     0       
# 2 5 100  # 100   100  -100     0     0  -100
# 3 4 100  # 100   100     0     0  -100  -100

# DiffArray  100  100    0    0  -100  -100
# PrefixSum  100*
# Max = 100

# DiffArray  100  100    0    0  -100  -100
# PrefixSum       200*
# Max = 200

# DiffArray  100  100    0    0  -100  -100
# PrefixSum            200
# Max = 200

# DiffArray  100  100    0    0  -100  -100
# PrefixSum                 200
# Max = 200

# DiffArray  100  100    0    0  -100  -100
# PrefixSum                       100
# Max = 200