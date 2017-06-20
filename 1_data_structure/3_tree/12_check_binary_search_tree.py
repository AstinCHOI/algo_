
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
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