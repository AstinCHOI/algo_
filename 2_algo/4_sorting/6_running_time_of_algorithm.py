n = int(input())
arr = list(map(int, input().split()))

t = 0
for i in range(1, n):
    k = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > k:
        arr[j+1] = arr[j]
        j = j-1
        t = t+1
    arr[j+1] = k
    
print(t)