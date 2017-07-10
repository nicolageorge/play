import sys

def solve(n, s, d, m):
    ret = 0
    if m == 1 and len(s) == 1:
        if d == s[0]:
            return 1
    for x in range(len(s)-m+1):
        if sum(s[x:x+m]) == d:
            ret += 1
    return ret

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split()
d, m = int(d), int(m)
print solve(n, s, d, m)
