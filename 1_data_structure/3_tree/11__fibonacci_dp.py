
# recursive
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# memozation
# top-down way
memo = [0 for _ in range(100)]
def fibonacci2(n):
    if n <= 1:
        return 1
    else:
        if memo[n] > 0:
            return memo[n]

        memo[n] = fibonacci(n-2) + fibonacci(n-1)
        return memo[n]

# Bottom-up way
def fibonacci3(n):
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


if __name__ == '__main__':
    print(fibonacci3(3))