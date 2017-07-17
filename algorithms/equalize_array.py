import sys
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

max_el = 0
max_char = ''
for el in set(a):
    occurances = a.count(el)
    if occurances > max_el:
        max_el = occurances
        max_char = el

print len(a) - max_el
