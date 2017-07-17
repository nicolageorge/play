import sys

def better_save_prisoner(prisoners, sweets, start):
    if prisoners == sweets:
        return start
    return start + ( sweets % prisoners ) - 1

def even_better_save_priz(prisoners, sweets, start):
    poisoned = (start + sweets - 1) % prisoners
    if poisoned == 0:
        poisoned = prisoners
    return poisoned

tests = int(raw_input().strip())
out = []
for a0 in xrange(tests):
    [n, m, s] = map(int, raw_input().strip().split(' '))
    out.append(even_better_save_priz(n, m, s))

for o in out:
    print o
