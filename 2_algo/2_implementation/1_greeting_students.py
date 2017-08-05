n = int(input())

for _ in range(n):
    point = int(input())
    
    m = point % 5
    if point >= 38 and m >= 3:
        print(point - m + 5)
    else:
        print(point)