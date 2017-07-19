q = int(input())

for _ in range(q):
    cityMap = {}
    n, m, libraryCost, roadCost = map(int, input().split())

    # input the self {1: [1], ..}
    for i in range(1, n+1):
        li = [i]
        cityMap[i] = li

    # make the graph
    for j in range(m):
        x, y = map(int, input().split())
        li1, li2 = cityMap[x], cityMap[y]
        if (li1 != li2):
            li1.extend(li2) # cityMap[x].extend(li2)
            for node in li2:
                cityMap[node] = li1
            # print(cityMap)
# 3 3 2 1
# 1 2
# 3 1
# 2 3
# 1st
# li1 = [1], li2 = [2]
# cityMap[1] = [1, 2]
# li1 = [1, 2]
# CityMap[2] = [1, 2]

# 2nd
# li1 = [3], li2 = [1, 2]
# CityMap[3] = [3, 1, 2]
# li1 = [3, 1, 2]
# CityMap[1] = [3, 1, 2]
# CityMap[2] = [3, 1, 2]

# 3rd
# skip due to li1 == li2
    if libraryCost < roadCost:
        print(n*libraryCost)
    else:
        cost = 0
# 1, 2, 3 -> (3, 1, 2)
        for lst in set(map(tuple, cityMap.values())):
            size = len(lst)
            if size > 0:
                cost += libraryCost + ((size-1) * roadCost)
                # cost = 2 + (2 * 1) = 4
                # 1 library, (size-1) roads
        print(cost)

# 2
# 3 3 2 1
# 1 2
# 3 1
# 2 3
# 6 6 2 5
# 1 3
# 3 4
# 2 4
# 1 2
# 2 3
# 5 6