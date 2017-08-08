import math

n = int(raw_input().strip())

squares_list = []
for i in xrange(1, n/2):
    square = int(math.pow(i, 2))
    if square < n:
        squares_list.append(square)
    else:
        break


numbers = []
while n > 0:
    for i in reversed(squares_list):
        if i <= n:
            n = n-i
            numbers.append(i)

print numbers
