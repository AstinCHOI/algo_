# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
arr = list(map(int, input().split()))

rightmost = arr[-1]
flag = True
for i in range(size-2, -1, -1):
    if arr[i] > rightmost:
        arr[i+1] = arr[i]
        print(' '.join(list(map(str, arr))))
    else:
        arr[i+1] = rightmost
        print(' '.join(list(map(str, arr))))
        flag = False
        break

if flag:
    arr[0] = rightmost
    print(' '.join(list(map(str, arr))))
        