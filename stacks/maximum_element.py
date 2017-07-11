# https://www.hackerrank.com/challenges/maximum-element/problem

import sys
class Node:
    def __init__(self, data=None, the_max=None):
        self.data = data
        self.the_max = the_max


inputs = int(raw_input().strip())

stac = []
cur_max = 0
for i in range(inputs):
    inp = map(int, raw_input().strip().split(' '))
    if inp[0] == 1:
        val = inp[1]
        if cur_max < val:
            cur_max = val
        el = Node(val, cur_max)
        stac.append(el)
    elif inp[0] == 2:
        stac.pop()
    elif inp[0] == 3:
        print stac[-1].the_max
    else:
        pass
