lst = [1, 2,3,4,1,1,23,1,231,23,123,1,423,42,123,45,5,34,5,41,231,23,1,4543,53,5,123,1]
lst = sorted(lst)
rez = [lst[0]]
for n in lst:
    if rez[-1] != n:
        rez.append(n)

print rez
