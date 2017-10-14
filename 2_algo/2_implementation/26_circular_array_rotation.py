n, k, q = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

for _ in range(q):
    idx = int(input())
    print(arr[((n-k+idx)%n)])

#1 2 3
#3 1 2
#2 3 1
    
#1 2 3 4
#4 1 2 3
#3 4 1 2

#2 3 4 1

