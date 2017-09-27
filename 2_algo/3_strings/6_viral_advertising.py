n = int(input())
likes = 0
shared = 5
for i in range(n):
    like = (shared // 2)
    
    likes += like
    shared = like * 3

print(likes)

# from discussion
# m = 2
# tot = 2
# for _ in range(1, input()):
#     m += m>>1
#     tot += m
# print tot

# https://stackoverflow.com/questions/2840593/how-do-i-find-the-millionth-number-in-the-series-2-3-4-6-9-13-19-28-42-63

# Here's how it works:
# floor(3x / 2)
# floor(2x/2 + x/2)
# floor(x + x/2)
# x + floor(x/2) --->{since x is int, see here}
# x + x>>1 -------->{bitwise shift right x by k = floor(x/2^k}