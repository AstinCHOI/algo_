
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
    if position == 0:
        head = Node(data, head)
    else:
        tmp = head
        for _ in range(position-1):
            tmp = tmp.next
        
        tmp.next = Node(data, tmp.next)
            
    return head