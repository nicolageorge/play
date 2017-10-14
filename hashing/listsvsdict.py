import random
lmt = 20000000

def get_list():
	global lmt
	return [x for x in range(lmt)]

def get_dict():
	global lmt
	return {x:x for x in range(lmt)}

def interpol_search(haystack, needle):
	lo, high = 0, len(haystack)-1
	while lo<=high and needle>haystack[lo] and needle<haystack[high]:
		mid = lo + int( float( (high-lo) / haystack[high]-haystack[lo] ) * (needle-haystack[lo]) )
		if haystack[mid] == needle:
			return "found {} in haystack".format(needle)
		elif haystack[mid] < needle:
			lo = mid+1
		elif haystack[mid] > needle:
			high = mid-1
	return '{} not found'.format(needle)

 


def check_in_ds(haystack, needle):
	if needle in haystack:
		print '{} e in lista'.format(needle)
	else:
		print '{} nu e in lista'.format(needle)

lst = get_list()
# dct = get_dict()

for i in range(20):
	nr = random.randint(1, lmt)
	# check_in_ds(lst, nr)
	interpol_search(lst, nr)
		
