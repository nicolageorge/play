#!/bin/python

import sys

def getTotalX(a, b):
    ret = 0
    for i in range(1, b[0]+1):
        if all([i % x == 0 for x in a]) and all([x % i == 0 for x in b]):
            ret += 1
    return ret

# n, m = raw_input().strip().split(' ')
# n, m = [int(n), int(m)]
# a = map(int, raw_input().strip().split(' '))
# b = map(int, raw_input().strip().split(' '))


a =[2, 4]
b = [16, 32, 96]
total = getTotalX(a, b)
print(total)
