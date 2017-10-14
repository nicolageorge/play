def getLuckyFloorNumber(n):
	f = 0
	for i in range(1, n+1):
		f += 1
		while '13' in str(f) or '4' in str(f):
			f += 1
	return f


print getLuckyFloorNumber(12)