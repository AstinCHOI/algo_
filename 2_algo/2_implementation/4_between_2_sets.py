# My silly solution
# n, m = map(int, input().split(' '))
# A = list(map(int, input().split(' ')))
# B = list(map(int, input().split(' ')))

# r = 0
# min_ = min(B)
# for i in range(1, min_+1):
#     if sum(list(map(lambda x: i % x, A))) == 0 and \
#         sum(list(map(lambda x: x % i, B))) == 0:
#         # print(i)
#         r = r + 1
# print(r)

# Better solution
import sys
from functools import reduce
# from fractions import gcd

input()
a = map(int,input().strip().split())
b = map(int,input().strip().split())

def gcd(x, y):
    while b > 0:
        a, b = a, a % b
    return a

lcm_a = reduce(lambda x,y: x*y//gcd(x,y), a)
gcd_b = reduce(gcd, b)
print(sum(1 for x in range(lcm_a, gcd_b+1, lcm_a) if gcd_b%x==0))

# GCD: Greate Common Devisor
# LCM: Lowest Common Multiple

# input
# 2 3
# 2 4
# 16 32 96

# output
# 3 (4,8,16)

