low = int(raw_input().strip())
high = int(raw_input().strip())
out = []

for n in range(low, high+1):
	sqr = n**2
	sqr_str = str(sqr)
 	if sqr_str[:len(sqr_str)/2].strip() == '':
		left = 0
	else:
		left = int(sqr_str[:len(sqr_str)/2].strip())
	right = int(sqr_str[len(sqr_str)/2:].strip()) if not '' else 0

	if left+right == n:
		out.append(n)

if len(out):
	print ' '.join(str(n) for n in out)
else:
	print 'INVALID RANGE'