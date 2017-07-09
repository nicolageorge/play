"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
class Copac(object):
	def __init__(self, data):
		self.data = data
		self.output = []
		self.left = None
		self.right = None
		
	def pre_traversal(self, nod):
		self.output.append(nod.data)
		if nod.left:
			self.pre_traversal(nod.left)
		if nod.right:
			self.pre_traversal(nod.right)
		
	def post_traversal(self, nod):
		if nod.left:
			self.post_traversal(nod.left)
		if nod.right:
			self.post_traversal(nod.right)
		self.output.append(nod.data)

	def in_traversal(self, nod):
		if nod.left:
			self.in_traversal(nod.left)
		self.output.append(nod.data)
		if nod.right:
			self.in_traversal(nod.right)
		
	def get_height(self, nod):
		if nod is None:
			return 0
		h_left = self.get_height(nod.left)
		h_right = self.get_height(nod.right)
		if h_left > h_right:
			return h_left+1
		else:
			return h_right+1

	def print_top_view(self, root):
		if not root:
			return
		curr = root
		left_list = []
		while curr:
			left_list.append(curr)
			curr = curr.left

		while len(left_list):
			curr = left_list.pop()
			self.output.append(curr.data)
		
		curr = root.right
		while curr:
			self.output.append(curr.data)
			curr = curr.right
		print ' '.join([str(x) for x in self.output])

	def insert(self, root, value):
		node = root
		if node is None:
			node = Copac(value)
			return node

		while True:
			if value > node.data:
				if node.right:
					node = node.right
				else:
					node.right = Copac(value)
					break
			if value < node.data:
				if node.left:
					node = node.left
				else:
					node.left = Copac(value)
					break
		return root


	def display(self):
		print ' '.join([str(c) for c in self.output])


def topView(root):
	tre = Copac(root.data)
	tre.print_top_view(root)

def insert(root, value):
	tre = Copac(root.data)
	return tre.insert(root, value)





root = Copac(4)
root.right = Copac(7)
root.left = Copac(2)
root.left.left = Copac(1)
root.left.right = Copac(3)
print insert(root, 0)

