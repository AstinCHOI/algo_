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
            li1.extend(li2)
            for node in li2:
                cityMap[node] = li1

    if libraryCost < roadCost:
        print(n*libraryCost)
    else:
        cost = 0
        
        for lst in set(map(tuple, cityMap.values())):
            size = len(lst)
            if size > 0:
                cost += libraryCost + ((size-1) * roadCost)

        print(cost)