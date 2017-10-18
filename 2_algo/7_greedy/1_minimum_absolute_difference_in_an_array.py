import sys

n = int(input())
arr = list(map(int, input().split(' ')))
m = sys.maxsize

## 1st try : timeout
# for i in range(n-1):
#     for j in range(i+1, n):
#         v = abs(arr[i] - arr[j])
#         if m > v:
#             m = v
# print(m)

arr.sort()
for i in range(1, n):
    v = abs(arr[i-1] - arr[i])
    if m > v:
        m = v
print(m)

## This is better
## the same logic with above code 
## from discussion
# n,a = input(),sorted(map(int, input().split()))
# print(min(abs(x-y) for x,y in zip(a,a[1:])))