"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def FindMergeNode(headA, headB):
    headALen = 0
    headBLen = 0
    headACopy = headA
    headBCopy = headB

    while headACopy is not None:
        headACopy = headACopy.next
        headALen += 1
    while headBCopy is not None:
        headBCopy = headBCopy.next
        headBLen += 1
    while headALen > headBLen:
        headA = headA.next
        headALen -= 1
    while headBLen > headALen:
        headB = headB.next
        headBLen -= 1
    while headA is not None:
        if headA == headB:
            return headA.data
        headA = headA.next
        headB = headB.next
    return -1
