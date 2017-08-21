#!/bin/python
# https://www.hackerrank.com/challenges/queens-attack-2
import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]



    # your code goes here
pr = n + n + n  - 4
print pr
