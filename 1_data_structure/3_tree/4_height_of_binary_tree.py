
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# def height(root):
#     if not root:
#         return -1
#     return max(height(root.left), height(root.right)) + 1

def height(root):
    lh = 0
    rh = 0
    
    if root.left:
        lh = 1 + height(root.left)
    
    if root.right:
        rh = 1 + height(root.right)
    
    return lh if lh > rh else rh

#           3      
#          / \
# (2)     2   5        (3 > 2)
#        /   / \   
# (1)   1   4   6      (2)
#      / \ / \ / \ 
# (0) None        7    (1)
#                  \
#                 None (0)
    