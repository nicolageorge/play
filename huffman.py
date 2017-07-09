class Node(object):
	def __init__(self, data, freq):
		self.freq = freq
		self.data = data
		self.left = None
		self.right = None

def decodeHuff(root, s):
   #Enter Your Code Here
	"""A - 1, B - 00, C - 01"""
	output = []
	base = root
	while len(s):
		if s[0] == '1':
			base = base.right
		else:
			base = base.left
		if len(s):
			s = s[1:]
		if base.left is None and base.right is None:
			output.append(base.data)
			base = root

	print "".join(output)

    
st = raw_input()
root = Node("root", 5)
root.left = Node("root", 2)
root.left.left = Node("B", 1)
root.left.right = Node("C", 1)
root.right = Node("A", "3")
decodeHuff(st, root)

