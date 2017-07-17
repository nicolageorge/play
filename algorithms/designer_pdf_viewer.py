#!/bin/python
import string
import sys

h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

# letter_index = string.lowercase.index(word[0])

maxim = 0
for c in word:
    if maxim < h[ string.lowercase.index(c) ]:
        maxim = h[ string.lowercase.index(c) ]

print maxim * len(word)
