import sys

def getRecord(s):
    lowest = s[0]
    highest = s[0]
    low_break = 0
    high_break = 0
    for r in s:
        if r < lowest:
            lowest = r
            low_break += 1
        if r > highest:
            highest = r
            high_break += 1
    return [high_break, low_break]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print ' '.join(map(str, result))
