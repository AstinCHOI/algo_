n, d = map(int, raw_input().split(' '))
arr = raw_input().split(' ')

for i in xrange(d):
    arr.append(arr[0])
    del arr[0]

print(' '.join(arr))


## Input
# 5 4
# 1 2 3 4 5

## Output
# 5 1 2 3 4