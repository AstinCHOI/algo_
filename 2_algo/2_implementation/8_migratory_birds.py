input()
types = list(map(int, input().split(' ')))

#1
birds = [0]*6
m = -1
idx = 0
for item in types:
    birds[item] += 1
    if m < birds[item]:
        m = birds[item]
        idx = item
    elif m == birds[item] and item < idx:
        idx = item

print(idx)

#2
#print( max( (types.count(i), i) for i in types )[1] )

#3
# import sys
# from collections import Counter
# birds = Counter(types)  # Counts the array into a dictionary
# print(birds.most_common(1)[0][0])

#4
# for t in types:
#     birds[t] += 1
# print(count.index(max(birds)))