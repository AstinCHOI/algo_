#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

# arr.reverse()
# print(' '.join(str(i) for i in arr))

print(' '.join(str(i) for i in arr[::-1]))

## Input
# 4
# 1 4 3 2

## Output
# 2 3 4 1
