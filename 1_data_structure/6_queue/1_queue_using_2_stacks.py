# q = int(input())
# Q = []

# for i in range(q):
#     line = input()
#     if line.startswith('1'):
#         Q.append(int(line.split(' ')[1]))
#     elif line.startswith('2'):
#         if Q:
#             Q = Q[1:]
#     elif line.startswith('3'):
#         if Q:
#             print(Q[0])

q = int(input())
s1 = []
s2 = []

def move(a, b):
    while a:
        b.append(a.pop())

for i in range(q):
    line = input()
    if line.startswith('1'):
        s1.append(int(line.split(' ')[1]))
    elif line.startswith('2'):
        if not s2:
            move(s1, s2)
        s2.pop()
    elif line.startswith('3'):
        if not s2:
            move(s1, s2)
        print(s2[-1]) # peek