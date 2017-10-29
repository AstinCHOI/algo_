N = int(input())
gem = set(input())
for _ in range(N-1):
    arr = set(input())
    gem = gem.intersection(arr)
print(len(gem))