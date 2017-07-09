"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
	node = head
	if head is None:
		return None
	while head.next is not None:
		if head.data == head.next.data:
			head.next = head.next.next
		else:
			head = head.next
	return node