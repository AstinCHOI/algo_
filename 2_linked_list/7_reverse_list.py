
"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        reverseHead = Reverse(head.next)
        head.next.next = head
        head.next = None
      
        return reverseHead

# ====================
#         h   r
# 1 > 2 > 3 > 4 > None
# ====================
# r    
# 4 > 3 > None
#     ^
# 1 > 2
#     h
# ====================
# r        
# 4 > 3 > 2 > None
#         ^
#         1
#         h
# ====================
# 4 > 3 > 2 > 1 > None
# ====================