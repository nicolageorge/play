#!/bin/python

import sys


t = int(raw_input().strip())

cur_time = 1
display_time = 3
old_display_time = 3

while cur_time < t:
    display_time -= 1
    cur_time += 1
    if display_time < 1:
        display_time, old_display_time = old_display_time * 2, display_time

print display_time

# https://www.hackerrank.com/challenges/strange-code
