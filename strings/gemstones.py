import sys

def gemstones(arr):
    if len(arr) == 0:
        return 0
    count = 0
    for elems in set(list(arr[0])):
        rock_count = 0
        for rocks in arr:
            rocks.find(elems)
            if rocks.find(elems) != -1:
                rock_count += 1
        if rock_count == len(arr):
            count += 1
    return count



n = int(raw_input().strip())
arr = []
arr_i = []
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print result
