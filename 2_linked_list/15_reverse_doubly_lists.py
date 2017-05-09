
"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
# def Reverse(head):
#     if head is None:
#         return None
#     elif head.next is None:
#         return head
    
#     node = Reverse(head.next)
#     head.prev = head.next
#     head.next.next = head
#     head.next = None
    
#     return node

def Reverse(head):
    while head:
        tmp = head
        head = head.next
        tmp.prev, tmp.next = tmp.next, tmp.prev
    return tmp