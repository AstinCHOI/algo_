L = int(input())
R = int(input())

# M = 0
# for i in range(L, R+1):
#     for j in range(L, R+1):
#         X = i ^ j
#         if X > M:
#             M = X
# print(M)


## from discussion
X = L ^ R
significantBit = X.bit_length()
result = (1 << significantBit) - 1
print(result)

# 10 > 1010
# 15 > 1111
# ----------
#  5 > 0101 (3 bit)
#  1 << 3 ==> 0b1000 - 1 = 7

# In other words,
# 1010
# 1111
# -X--
# 0111 = 7


# To maximize A xor B, we want A and B to differ as much as possible at every bit index.
# We first find the most significant bit that we can force to differ by looking at L and R.
# For all of the lesser significant bits in A and B, we can always ensure that they differ and still have L <= A <= B <= R.
# Our final answer will be the number represented by all 1s starting from the most significant bit that differs between A and B
# Let's try an example
#   L = 10111   
#   R = 11100
#       _X___  <-- that's most significant differing bit
#       01111  <-- here's our final answer
# Notice how we don't directly calculate the values of A and B.