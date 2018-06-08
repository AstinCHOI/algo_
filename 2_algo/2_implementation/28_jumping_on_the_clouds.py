energy = 100
n, k = map(int, input().split(' '))
clouds = list(map(int, input().split(' ')))

for i in range(0, n, k):
    if clouds[i] == 0:
        energy -= 1
    else:
        energy -= 3
print(energy)