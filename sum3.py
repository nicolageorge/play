#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    ret = [0, 0]
    if a0 > b0:
        ret[0] = 1
    if b0 < a0:
        ret[1] = 1
    if a1 > b1:
        ret[0] = ret[0] + 1
    if a1 < b1:
        ret[1] = ret[1] + 1
    if a2 > b2:
        ret[0] = ret[0] + 1
    if a2 < b2:
        ret[1] = ret[1] + 1
    return ret[0], ret[1]



a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
