"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

# def MergeLists(headA, headB):
#     head = Node()
#     cur = head
#     while (headA and headB):
#         if (headA.data < headB.data):
#             cur.next = Node(headA.data)
#             cur = cur.next
#             headA = headA.next
#         else: # (headA.data >= headB.data):
#             cur.next = Node(headB.data)
#             cur = cur.next
#             headB = headB.next
        
#     while headA:
#         cur.next = Node(headA.data)
#         cur = cur.next
#         headA = headA.next
    
#     while headB:
#         cur.next = Node(headB.data)
#         cur = cur.next
#         headB = headB.next
        
#     return head.next

def MergeLists(headA, headB):
    head = None
    if headA and (headB is None):
        return headA
    elif (headA is None) and headB:
        return headB
    else:
        if headA.data < headB.data:
            head = headA
            head.next = MergeLists(headA.next, headB)
        else: #headA.data >= headB.data:
            head = headB
            head.next = MergeLists(headA, headB.next)

    return head