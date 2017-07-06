#!/bin/python

import sys


# s,t = raw_input().strip().split(' ') # 7, 11
# s,t = [int(s),int(t)]
# a,b = raw_input().strip().split(' ') # 5, 15
# a,b = [int(a),int(b)]
# m,n = raw_input().strip().split(' ') # 3 , 2
# m,n = [int(m),int(n)]
# apple = map(int,raw_input().strip().split(' ')) # -2 2 1
# orange = map(int,raw_input().strip().split(' ')) # 5 -6

# print "s", s
# print "t", t
#
# print "a", a
# print "b", b
#
# print "m", m
# print "n", n
s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apple = [-2, 2, 1]
orange = [5, -6]

def checkFruit(s, t, a, b, m, n, apple, orange):
    apples = 0
    oranges = 0
    for ap in apple:
        if s <= ap+a <= t:
            apples += 1
    for o in orange:
        # print o
        if b - s >= abs(o) >= b - t and o < 0 :
            oranges += 1
    print apples
    print oranges

checkFruit(s, t, a, b, m, n, apple, orange)
