class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def in_order_traversal(self, root):
        if root is None:
            return None
        print root.value
        if root.left:
            self.in_order_traversal(root.left)
        if root.right:
            self.in_order_traversal(root.right)

class Codec:
    def __init__(self):
        self._null_placeholder = 'X'
        self._separator = ','
        self._list_tree = []

    def serialize(self, top_node):
        self._list_tree = []
        self._tree_to_string(top_node, self._list_tree)
        tree_string = ''.join([str(x) for x in self._list_tree])
        print tree_string
        return tree_string

    def deserialize(self, inp_string):
        nodes = inp_string.split(self._separator)
        root = self._build_tree(nodes)
        return root

    def _tree_to_string(self, top_node, list_tree):
        if top_node is None:
            self._list_tree.append(self._null_placeholder)
            self._list_tree.append(self._separator)
        else:
            self._list_tree.append(top_node.value)
            self._list_tree.append(self._separator)
            self._tree_to_string(top_node.left, self._list_tree)
            self._tree_to_string(top_node.right, self._list_tree)

    def _build_tree(self, nodes):
        val = nodes.pop(0)
        if val == self._null_placeholder or val == '':
            return None
        else:
            nod = Node(int(val))
            nod.left = self._build_tree(nodes)
            nod.right = self._build_tree(nodes)
            return nod


root = Node(40)
root.left = Node(30)
root.right = Node(50)

root.left.left = Node(20)
root.left.right = Node(35)

root.right.left = Node(45)
root.right.right = Node(55)

root.in_order_traversal(root)
#
codec = Codec()
serialized = codec.serialize(root)
new_root = codec.deserialize(serialized)
print new_root
root.in_order_traversal(new_root)
