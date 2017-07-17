import sys

nums = map(raw_input().strip().split())
ret = []

for i, num in enumerate(nums):
	if i == 0:
		ret.append(num)
	else:
		val = num - nums[i-1]
		if abs ( val ) >= 127:
			ret.append(-128)

		ret.append( val )

print ' '.join( [str(x) for x in ret] )