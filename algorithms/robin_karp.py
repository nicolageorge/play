import random
import string
class RobinKarp:
	def __init__(self):
		self._prime = 3
		self._lets = {}
		for i in range(len(string.ascii_letters)):
			self._lets[ string.ascii_letters[i] ] = i

	def _hash(self, inp):
		has = 0
		p = 0
		for i in range(len(inp)):
			o = self._lets[inp[i]]
			if o < 0:
				raise ValueError('o is smaller than 0')
			has += o * self._prime**p
			p += 1
		return has
	
	def find_substring(self, haystack, needle):
		needle_hash = self._hash(needle)
		hay_hash = self._hash(haystack[0:len(needle)])

		# print needle_hash, hay_hash

		for i in range(len(haystack) - len(needle)):
			# print 'neeldehash', needle_hash, 'hayhash', hay_hash
			if needle_hash == hay_hash:
				if neelde == haystack[i:i+len(needle)]:
					print i
					print haystack[i-10:i+len(needle)+10]
			hay_hash -= self._lets[haystack[i]]
			print 'hh1', hay_hash
			hay_hash /= self._prime
			print 'hh2', hay_hash
			hay_hash += self._lets[haystack[i+len(needle)]] * self._prime**len(needle)
			print 'hh3', hay_hash
				
rk = RobinKarp()

# haystack = ''.join([random.choice(string.ascii_letters) for x in range(3999999)])
haystack = ''.join([random.choice(string.ascii_letters) for x in range(99)])
# needle = raw_input('enter search string...').strip()
print haystack
needle = 's'
rk.find_substring(haystack, needle)

