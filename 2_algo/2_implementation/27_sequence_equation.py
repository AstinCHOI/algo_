n = int(input())
arr = list(map(int, input().split()))
invs = [0] * (n+1)

for i in range(1, n+1):
    invs[arr[i-1]] = i

for i in range(1, n+1):
    print(invs[invs[i]])