"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
class Copac(object):
	def __init__(self, nod):
		self._node = nod
		self.output = []
		
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

	def top_view(self, root, hd, level):
		if not root:
			return
		if hd in self.m:
			if level < self.m[hd][1]:
				self.m.update( {hd: [root.data, level]} )
			else:
				self.m[hd] = [root.data, level]
			print m
		self.top_view(root.left, hd-1, level+1)
		self.top_view(root.right, hd+1, level+1)

	def print_top_view(self, root):
		self.m = {}
		self.top_view(root, 0, 0)
		print self.m


	def display(self):
		print ' '.join([str(c) for c in self.output])


def topView(root):
	tre = Copac(root)
	tre.print_top_view(root)