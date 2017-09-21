n = int(input())
st = input()

se = set()
for al in st:
    se.add(al)

se = list(se)
sel = len(se)

def check_two(a, b):
    val = a
    two = ''
    for al in st:
        if al == a or al == b:
            two += al  
    
    pre = ''
    flag = True

    for one in two:
        if pre == one:
            flag = False
            break
        pre = one
                
    return len(two) if flag else 0

m = [0]
for i in range(sel):
    for j in range(i+1, sel):
        m.append(check_two(se[i], se[j]))
        
print(max(m))