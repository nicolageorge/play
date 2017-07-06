#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    meetingPoint = 0
    if (x1 < x2 and v1 < v2) or (x1 > x2 and v1 > v2):
        return 'NO'

    for t in range(1000):
        if(x1 + v1*t) == (x2+v2*t):
            return 'YES'
    return 'NO'

# x1, v1, x2, v2 = raw_input().strip().split(' ')
# x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

x1, v1, x2, v2 = 4602, 8519, 7585, 8362
result = kangaroo(x1, v1, x2, v2)
print(result)
