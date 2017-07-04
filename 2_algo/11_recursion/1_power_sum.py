# O(x^(1 + 1/n))

# x = int(input())
# n = int(input())

# dp = [1] + [0] * x

# for i in range(1, int(pow(x, 1/n)) + 1):
#     u = i ** n
#     for j in range(x, u-1, -1):
#         dp[j] += dp[j-u]
# print(dp[-1])


# 10
# 2
# ===
# for i in range(1, 4):
# u = 1 ** 2
# for j in range(10, 0, -1):
#   dp[10] += dp[9]
#   dp[9] += dp[8]
#   ...
#   dp[1] += dp[0]
# [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# u = 2 ** 2
# for j in range(10, 3, -1):
# dp[10] += dp[10-4]
# dp[9] += dp[9-4]..
# [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0]

# u = 3 ** 2
# for j in range(10, 8, -1):
# dp[10] += dp[10-9]
# dp[9] += dp[9-9]..
# [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]


def powerSum(total, power, num):
    value = total - (num ** power)

    if value < 0:
        return 0
    elif value == 0:
        return 1
    else:
        return powerSum(value, power, num+1) + powerSum(total, power, num+1)

total = int(input())
power = int(input())

print(powerSum(total, power, 1))

# 10
# 2

# (10, 2, 1) $1
#    \/
# (9, 2, 2) $2 + (10, 2, 2) $5 -> (4, 2, 3) $6 + (10, 2, 3) $7 -> (1, 2, 4) $8 + (10, 2, 4) $9
#    \/
# (5, 2, 3) $3 + (9, 2, 3) $4

# "$4" returns "1"