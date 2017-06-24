# O(N^2) when finding maximum element
# N = int(input())
# s = []

# for i in range(N):
#     line = input()
#     if line.startswith('1'):
#         s.append(int(line.split(' ')[1]))
#     elif line.startswith('2'):
#         if s:
#             s.pop()
#     elif line.startswith('3'):
#         if s:
#             print(max(s))

# O(1) when finding maximum element
class Hello:
    def __init__(self, val, m):
        self.val = val
        self.m = m

N = int(input())
s = []
m = -1

for i in range(N):
    line = input()
    if line.startswith('1'):
        val = int(line.split(' ')[1])
        a = Hello(val, m)
        if val >= m:
            m = val
        s.append(a)
    elif line.startswith('2'):
        if s:
            a = s.pop()
            if a.val == m:
                m = a.m
    elif line.startswith('3'):
        if s:
            print(m)