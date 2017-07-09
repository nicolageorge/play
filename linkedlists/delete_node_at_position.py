"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
	root = head
	if position == 0:
		return root.next
	else:
		while position > 1:
			root = root.next
			position -= 1
		root.next = root.next.next
		return head

  
  
  
  
  
  
