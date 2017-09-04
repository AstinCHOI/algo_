n = int(input())
arr = list( map(int, input().split(' ')) )

a = [0] * 100
# k, v = -1, -1 # FAIL
for item in arr:
    a[item] += 1
    # k = item
    # v = a[item]
    
# FAIL
# n = 0
# try:
#     if a[k-1] > a[k+1]:
#         n = a[k-1]
#     else:
#         n = a[k+1]
# except:
#     n = a[k-1]

# print(v+n)

m = 0
for i in range(1, 100):
    if a[i] >= 1:
        s = a[i-1] + a[i]
        if s > m:
            m = s
print(m)