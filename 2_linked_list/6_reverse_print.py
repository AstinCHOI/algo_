
"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

# def ReversePrint(head):
#     if head is None:
#         return
#     arr = []
#     while head:
#         arr.append(head.data)
#         head = head.next
#     arr.reverse()
#     for data in arr:
#         print(data)


# def ReversePrint(head):
#     if head is None:
#         return
#     else:
#         ReversePrint(head.next)
#         print(head.data)

def ReversePrint(head):
    if head:
        ReversePrint(head.next)
        print(head.data)