"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    node = r
    if node is None:
        node = Node(data=data)
        return node
    while True:
        if val > node.data:
            if node.right is not None:
                node = node.right
            else:
                node.right = Node(data=val)
                break
        else:
            if node.left is not None:
                node = node.left
            else:
                node.left = Node(data=val)
                break
    return r
