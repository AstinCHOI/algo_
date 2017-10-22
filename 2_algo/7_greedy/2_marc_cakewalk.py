n = int(input())
cakes = list(map(int, input().split(' ')))

cakes.sort(reverse=True)
mile = 0
for i in range(n):
    mile += cakes[i] * 2 ** i
print(mile)

# print(sum(c * 2 ** j for (j, c) in enumerate(cakes, reverse=True))))