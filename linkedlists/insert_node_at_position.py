"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
	root = head
	if position == 0:
		nod = Node(data=data)
		nod.next = head
		return nod
	else:
		while position > 1:
			root = root.next
			position -= 1

		aux = root.next
		root.next = Node(data=data)
		root.next.next = aux
		return head
 