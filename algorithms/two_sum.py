nums = [2, 7, 11, 15]
target = 9

for n in nums:
    if target-n in nums:
        print n, target-n
        break
else:
    print "does not exist"
