#!/bin/python

import sys

def fines(ret_d, ret_m, ret_y, exp_d, exp_m, exp_y):
    if ret_y > exp_y:
        return 10000
    elif ret_y == exp_y:
        if ret_m > exp_m:
            return 500 * (ret_m - exp_m)
        elif ret_m == exp_m:
            if ret_d > exp_d:
                return 15 * (ret_d - exp_d)
            else:
                return 0
        else:
            return 0
    else:
        return 0


d1,m1,y1 = raw_input().strip().split(' ')
ret_d, ret_m, ret_y = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
exp_d, exp_m, exp_y = [int(d2),int(m2),int(y2)]

print fines(ret_d, ret_m, ret_y, exp_d, exp_m, exp_y)
