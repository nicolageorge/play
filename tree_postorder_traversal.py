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
		


	def display(self):
		print ' '.join([str(c) for c in self.output])


def inOrder(root):
    #Write your code here
	# print root
    #Write your code here
    tre = Copac(root)
    tre.in_traversal(root)
    tre.display()
