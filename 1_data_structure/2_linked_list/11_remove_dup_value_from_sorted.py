
"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

# def RemoveDuplicates(head):
#     tmp = head
    
#     if (head is None) or (head.next is None):
#         return head
    
#     while tmp.next is not None:
#         if tmp.data == tmp.next.data:
#             tmp.next = tmp.next.next
#         else:
#             tmp = tmp.next
    
#     return head
    
def RemoveDuplicates(head):
    h = None

    if (head is None) or (head.next is None):
        return head
    else:
        if head.next is not None:
            if head.data == head.next.data:
                if (head.next.next is not None) and (head.data == head.next.next.data):
                    h = RemoveDuplicates(head.next.next.next)
                else:
                    h = head
                    h.next = RemoveDuplicates(head.next.next)
            else:
                h = head
                h.next = RemoveDuplicates(head.next)

    return h

#   _   _   _
# h h   h   h   h h        
# 1 2 2 2 2 2 2 2 3

# h h   h   h
# 1 2 2 3 3 4