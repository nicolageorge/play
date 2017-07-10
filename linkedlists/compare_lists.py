#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
	if headA is None and headB is None:
		return 1
	while headA.data == headB.data:
		if headA.next is None:
			if headB.next is None:
				return 1
			else:
				return 0
		headA = headA.next
		headB = headB.next
	return 0