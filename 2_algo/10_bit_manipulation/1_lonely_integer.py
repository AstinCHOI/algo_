from functools import reduce


n = int(input())
arr = map(int, input().split())

res = reduce((lambda x, y: x^y), arr)
print(res)

# XOR 
# 0^0=0, 1^1=0
# 0^1=1, 1^0=1

# 0 0 1 2 1
# 0^0 = 0
# 0^1 = 1
# 01 ^ 10 = 11
# 11 ^ 01 = (10)

# Finally, remain the different number because the result of the same pair is 0
# 0 ^ different number = different number