s = input()
n = int(input())

query = []
pre = 0
for one in s:
    o = ord(one)-96
    if pre == o:
        query.append(query[-1] + o)
    else:
        query.append(o)
    pre = o

for _ in range(n):
    q = int(input())
    if q in query:
        print("Yes")
    else:
        print("No")
    