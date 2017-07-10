"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
         4
       /   \
      2     7
     / \   /
    1   3 6
v1 = 1 and v2 = 3
"""
def lca(root , v1 , v2):
	if root is None:
		return None
	if v1 > v2:
		v1, v2 = v2, v1
	while root.data < v1 or root.data > v2:
		if root.data < v1:
			root = root.left
		else:
			if root.data > v2:
				root = root.right
	return root