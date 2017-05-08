
"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""

# def SortedInsert(head, data):
#     if head is None:
#         return Node(data)
#     elif data < head.data:
#         node = Node(data, head)
#         head.prev = node
#         return node

#     next = SortedInsert(head.next, data)
#     head.next = next
#     next.prev = head
#     return head

def SortedInsert(head, data):
    h = head
    
    if h is None:
        return Node(data)
    elif data < h.data:
        node = Node(data, h)
        h.prev = node
        return node
            
    while h.next is not None:
        if data < h.next.data:
            node = Node(data, h.next, h)
            h.next = h.next.prev = node
            return head
        
        h = h.next
    
    h.next = Node(data, None, h)
    
    return head