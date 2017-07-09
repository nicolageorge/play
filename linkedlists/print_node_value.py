#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
	nodes = 0
	i = head
	while i is not None:
		i = i.next
		nodes += 1
	nodes -= position

  	while nodes > 1:
		node = node.next
  		nodes -= 1
  	return node
