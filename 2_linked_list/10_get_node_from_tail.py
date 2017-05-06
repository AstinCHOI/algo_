
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

# def GetNode(head, position):
#     if head is None:
#         return None
    
#     tmp = head
#     i = 0
#     while tmp:
#         i += 1
#         tmp = tmp.next
  
#     for _ in range(i-position-1):
#         head = head.next
  
#     return head.data

def GetNode(head, position):
    if head is None:
        return None

    arr = []
    while head:
        arr.append(head.data)
        head = head.next

    return arr[(position * -1) - 1]