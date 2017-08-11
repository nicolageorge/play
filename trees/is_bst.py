""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

INT_MAX = 4294967296
INT_MIN = -4294967296
def check_binary_search_tree_(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))

# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))


import sys

def check_binary_search_tree_(node):
    return is_valid_bst(node, sys.maxint * -1, sys.maxint)

def is_valid_bst(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return is_valid_bst(node.left, mini, node.data - 1) and is_valid_bst(node.right, node.data+1, maxi)





























def check_binary_search_tree_(node):
    return vld_bst(node, -1 * sys.maxint, sys.maxint)

def vld_bst(node, minimum, maximum):
    if node is None:
        return True

    if node.data < minimum or node.data > maximum:
        return False

    return vld_bst(node.left, minimum, node.data - 1) and vld_bst(node.right, node.data +1, maximum)
