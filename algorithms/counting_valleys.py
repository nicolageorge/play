import sys

inputs = int(raw_input().strip())
route = raw_input().strip()
valley_counter = 0
level = 0
for c in route:
    if c == 'U':
        level += 1
        if level == 0:
            valley_counter += 1
    if c == 'D':
        level -= 1

print valley_counter
