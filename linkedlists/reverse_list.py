"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
	if head is None:
		return None
	node = None
	while head is not None:
		i = node
        
		node = Node()
		node.data = head.data
		node.next = i
		# print node.data

		head = head.next
	return node



[2, 3, 4, 5, 6, 7, 8]