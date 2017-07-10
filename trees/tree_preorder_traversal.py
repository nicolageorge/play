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
		
	def traversal(self, nod):
		self.output.append(nod.data)
		if nod.left:
			self.traversal(nod.left)
		if nod.right:
			self.traversal(nod.right)

	def display(self):
		print ' '.join([str(c) for c in self.output])


def preOrder(root):
	# print root
    #Write your code here
    tre = Copac(root)
    tre.traversal(root)
    tre.display()