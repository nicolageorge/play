lst = [1, 2,3,4,1,23,1,231,23,123,1,423,42,123,45,5,34,5,41,231,23,1,4543,53,5,123,1]
print set(lst)
el = 1
shifts = 0


slow = 0
for fast in range(len(lst)):
    if lst[fast] != el:
        lst[slow] = lst[fast]
        slow += 1

print lst[:slow]
