
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
#1
def check(root, mn, mx):
    if root:
        if root.data >= mx or root.data <= mn:
            return False
        else:
            return check(root.left, mn, root.data) and \
                check(root.right, root.data, mx)
    else:
        return True

def check_binary_search_tree_(root):
    import sys
    return check(root, 0, sys.maxsize)


#2
recent = 0
def check_binary_search_tree_(root):
    global recent
    if root is None:
        return True

    flag = check_binary_search_tree_(root.left)

    if flag:
        if recent >= root.data:
            return False
        else:
            recent = root.data

        flag = check_binary_search_tree_(root.right)

    return flag

# Case 1 :
#    20
#   /  \
#  10   2

# Case 2:
#    18
#   /  \
#  8    20
#      /  \
#     10  30
