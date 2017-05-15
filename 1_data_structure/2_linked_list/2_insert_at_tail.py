
"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

# def Insert(head, data):
#     if head is None:
#         head = Node(data)
#     else:
#         if head.next is None:
#             head.next = Node(data)
#         else:
#             Insert(head.next, data)
#     return head

def Insert(head, data):
    if head is None:
        head = Node(data)
    else:
        tmp = head
        while tmp:
            if tmp.next is None:
                tmp.next = Node(data)
                break
            else:
                tmp = tmp.next
    return head