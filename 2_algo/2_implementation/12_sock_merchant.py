def sockMerchant(n, ar):
    d = {}
    tot = 0
    for item in ar:
        if item not in d.keys() or d[item] == 0:
            d[item] = 1
        else:
            d[item] = 0
            tot += 1
    return tot

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)