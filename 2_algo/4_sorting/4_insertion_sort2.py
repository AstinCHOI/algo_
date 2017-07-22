n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    k = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > k:
        arr[j+1] = arr[j]
        j = j-1        
    arr[j+1] = k
    
    # print(' '.join(list(map(str, arr))))
    print(*arr)

# 6
# 1 4 3 5 6 2

# 1 4 3 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 2 3 4 5 6