q = int(input())

for _ in range(q):
    num = input()
    lnum = len(num)
    
    flag = False
    d = 0
    for i in range(1, (lnum//2)+1):
        d = int(num[:i])
        expected = d + 1
        j = i
        while j < lnum:
            lexp = len(str(expected))
            nxt = j+lexp
            if expected == int(num[j:nxt]):
                j = nxt
                expected += 1
                flag = True
            else:
                flag = False
                break
        if flag:
            break
    if flag:
        print("{0} {1}".format("YES", d))
    else:
        print("NO")