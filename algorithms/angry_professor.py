import sys

def check_students(k, a):
    counter = 0
    for stud_time in a:
        if stud_time <= 0:
            counter += 1
            if counter >= k:
                return 'NO'
    return 'YES'

def check_studs(k, a):
    early_students = [x for x in a if x <=0]
    if k <= len(early_students):
        return 'NO'
    else:
        return 'YES'


t = int(raw_input().strip())
for a0 in xrange(t):
    [n, k] = map(int, raw_input().strip().split(' '))
    a = map(int, raw_input().strip().split(' '))
    print check_studs(k, a)
