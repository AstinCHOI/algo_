x1, v1, x2, v2 = map(int, input().split(' '))

# 1st try: fail
# if (x1 == x2 and v1 != v2) or (x1 != x2 and v1 == v2):
#     print("NO")
# elif (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2):
#     print("NO")
# else:
# 	# ...
#     print("YES")

# 2st
if v1 > v2 and ((x2 - x1) % (v1 - v2) == 0):
    print("YES");
else:
    print("NO");

# y is the number of jumps
# x1 + (y * v1) == x2 + (y * v2)
# => x1 - x2 == (y * v2) - (y * v1) 
# => x1 - x2 == y(v2 - v1)
# => x2 - x1 == y(v1 - v2) ,because x1 < x2
# => (x2 - x1) / (v1 - v2) == y
# so, (x2 - x1) % (v1 - v2) == 0 -> OK