q = int(input())

hackerrank = 'hackerrank'
hLen = len(hackerrank)
for _ in range(q):
    s = input()
    l = 0
    for a in s:
        if l < hLen and hackerrank[l] == a:
            l += 1
            if hLen == l:
                break
    if hLen == l:
        print("YES")
    else:
        print("NO")