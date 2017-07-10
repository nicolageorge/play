import sys

def migratoryBirds(n, ar):
    values = {}
    for x in ar:
        if x in values:
            values[x] += 1
        else:
            values[x] = 1
    freq = 0
    item = None
    for i, e in values.items():
        if e > freq:
            item, freq = i, e
    return item
# 1 4 4 4 5 3

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
print migratoryBirds(n, ar)
