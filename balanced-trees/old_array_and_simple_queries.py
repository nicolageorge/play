import sys

def prepend_action(arr, i, j):
    ret = arr[i:j]
    ret.extend(arr[:i])
    ret.extend(arr[j:])
    return ret

def append_action(arr, i, j):
    ret = arr[:i]
    ret.extend(arr[j:])
    ret.extend(arr[i:j])
    return ret


[n, m] = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))

for k in range(m):
    [tp, i, j] = map(int, raw_input().strip().split(' '))
    i -= 1
    # j -= 1

    if tp == 1:
        arr = prepend_action(arr, i, j)
    if tp == 2:
        arr = append_action(arr, i, j)
    # print ' '.join([str(x) for x in arr])

print abs(arr[0]-arr[n-1])
print ' '.join([str(x) for x in arr])



#
# 8 4
# 1 2 3 4 5 6 7 8
# 1 2 4
# 2 3 5
# 1 4 7
# 2 1 4
