
"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

# def FindMergeNode(headA, headB):
#     a = headA
#     while headA:
#         if headA == headB:
#             return headA.data
#         headA = headA.next

#     return FindMergeNode(a, headB.next)


def FindMergeNode(headA, headB):
    arr = []

    while headA:
        arr.append(headA)
        headA = headA.next

    while headB:
        for a in arr:
            if a == headB:
                return a.data

        headB = headB.next

# 
# 1--->2
#       \
#        3--->Null
#       /
#      1