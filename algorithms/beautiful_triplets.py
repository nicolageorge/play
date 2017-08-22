[n, diff] = map(int, raw_input().strip().split(' '))
nums = map(int, raw_input().strip().split(' '))

d = {}
for i in nums:
	d[i] = True

ret = 0
for i in nums:
	if i + diff in d and i + (2*diff) in d:
		# print i, i+diff, i + (2 * diff)
		ret += 1
print ret