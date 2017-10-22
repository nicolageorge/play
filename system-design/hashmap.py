import unittest

def print_data(func):
	def wrapper(*args, **kwargs):
		print args[0]._data
		rv = func(*args, **kwargs)
		print args[0]._data
		print "---------------end execution------------------"
		return rv
	return wrapper


class Item:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __repr__(self):
		return "({}:{})".format(self.key, self.value)


class Hashmap:
	def __init__(self):
		self._hash_mod = 9187
		self._data = [[] for i in range(self._hash_mod)]
		
	def _hash_function(self, key):
		return key % self._hash_mod

	# @print_data
	def get(self, key):
		k = self._hash_function(key)
		for _ in self._data[k]:
			if _.key == key:
				return _.value
		else:
			raise ValueError("inexistent key")

	# @print_data
	def set(self, key, value):
		k = self._hash_function(key)
		for _ in self._data[k]:
			if _.key == key:
				_.value = value
				break
		else:
			self._data[k].append(Item(key, value))


	def delete(self, key):
		k = self._hash_function(key)
		for index, item in enumerate(self._data[k]):
			if item.key == key:
				i = self._data[k].pop(index)
				return i
		else:
			raise ValueError("pop no key")


	def status(self):
		print self._data



# h = Hashmap()
# for i in range(200000):
# 	h.set(i, i**5)

# print h.get(123412)


class Test(unittest.TestCase):
	def test_1(self):
		h = Hashmap()
		for _ in range(300000):
			h.set(_, _*_+_)
		self.assertEqual( h.get(3143), 3143*3143+3143 )

if __name__=='__main__':
	unittest.main()





