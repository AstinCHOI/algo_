# Enter your code here. Read input from STDIN. Print output to STDOUT
V = int(input())
n = int(input())
arr = list(map(int, input().split(' ')))

for i in range(len(arr)):
    if arr[i] == V:
        print(i)
        break