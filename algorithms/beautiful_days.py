import sys
def reverse_number(n):
    return int(str(n)[::-1])

[start, end, div] = map(int, raw_input().strip().split(' '))

counter = 0
for i in range(start, end+1, ):
    if ( i - reverse_number(i) ) % div == 0:
        counter += 1
print counter
