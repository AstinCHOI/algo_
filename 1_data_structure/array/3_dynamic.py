#!/bin/python

import sys

N, Q = map(int, raw_input().strip().split(' '))
lastans = 0
seq = []
for arr_i in xrange(N):
    seq.append([])

for arr_i in xrange(Q):
    line = map(int, raw_input().strip().split(' '))
    
    f = (line[1] ^ lastans) % N
    if line[0] == 1:
        seq[f].append(line[2])
    elif line[0] == 2:
        lastans = seq[f][line[2] % len(seq[(line[1] ^ lastans) % N])]
        print lastans

## Input
# 2 5
# 1 0 5
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1

## Output
# 7
# 3