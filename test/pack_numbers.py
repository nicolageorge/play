def packNumbers(arrr):
	arr = list(arrr)
	arr.append(None)
	cur = arr[0]
	cnt = 0
	ret = []
	for _ in range(len(arr)):
		i = arr[_]
		if i == cur:
			cnt += 1
		else:
			if cnt > 1:
				ret.append('{}:{}'.format(cur, cnt))
				cnt = 1
			else:
				ret.append(cur)
		cur = i

	return ret


print packNumbers([5, 5, 5, 7, 7, 3, 4, 7])