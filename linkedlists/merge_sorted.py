"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
	if headA.data is None:
		return headB
	if headB.data is None:
		return headA

	if headA.data < headB.data:
		headA.next = MergeLists(headA.next, headB)
		return headA

  
  
  
  
  
  
  
  
  
  
  
