
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
    if head == None:
        return None
    elif position == 0:
        head = head.next
    else:
        tmp = head
        for _ in range(position-1):
            tmp = tmp.next
        
        if tmp.next is None:
            tmp = None
        else:
            tmp.next = tmp.next.next
    
    return head