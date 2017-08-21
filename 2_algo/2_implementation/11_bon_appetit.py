n, k = map(int, input().split(' '))
costs = list(map(int, input().split(' ')))
anna = int(input())

pay = 0
for i in range(n):
    if i == k:
        continue
    pay += costs[i]

dutch = int(pay / 2)

if dutch == anna:
    print("Bon Appetit")
else:
    print(anna - dutch)