# iterate through the list
# for each element found, find other two which sum up to negative element


arr = [1, 2, 3, -3, 2, 1, 3, -1, 0]

for n in arr:
    target = n
    for n1 in arr:
        if n1 != n:
            needle = -1 * (target + n1)
            if needle != n1 and needle != n:
                if needle in arr:
                    print n, n1, needle
