# import sys
# sys.setrecursionlimit(5000)

line = list(map(int, input().split(' ')))
arr = [-1 for _ in range(20)]

#1
def fibonacci(n):
    if n == line[0]:
        return line[0]
    elif n == line[1]:
        return line[1]
    else:
        return (fibonacci(n-1) ** 2) + fibonacci(n-2)
# print(fibonacci(line[2]-1))

#2
def fibonacci2(n):
    if arr[n] != -1:
        return arr[n]    
    else:
        arr[n] = (fibonacci2(n-1) ** 2) + fibonacci2(n-2)
        return arr[n]
    
arr[:2] = line[:2]
# print(fibonacci2(line[2]-1))

#3
s = line #
tn = s[2]
s1 = s[0]
s2 = s[1]
counter = [s1,s2]
for i in range(tn-2):
    counter.append(counter[i] + counter[i+1]**2)

print(counter[-1])