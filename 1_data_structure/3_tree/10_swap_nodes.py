
import queue
import sys

sys.setrecursionlimit(1500)

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def swap_node(root, k, atHeight):
    if root:
        if atHeight % k == 0:
            root.left, root.right = root.right, root.left

        swap_node(root.left, k, atHeight + 1)
        print(root.data, end=' ', flush=True)
        swap_node(root.right, k, atHeight + 1)

        return root

## Convert Queue to Tree
N = int(input())
root = Node(1)
q = queue.Queue()
q.put(root)
for i in range(N):
    a, b = map(int, input().split(' '))

    node = q.get()

    if a != -1:
        node.left = Node(a)
        q.put(node.left)

    if b != -1:
        node.right = Node(b)
        q.put(node.right)

## Swap and Inorder
K = int(input())
for _ in range(K):
    k = int(input())
    atHeight = 1
    root = swap_node(root, k, atHeight)
    print()

# Swap operation: Given a tree and a integer,
# K, we have to swap the subtrees of all the nodes who are at depth h, 
# where h ∈ [K, 2K, 3K,...].

#          1                     1                          1             
#         / \                   / \                        / \            
#        /   \                 /   \                      /   \           
#       2     3    [s]        2     3                    2     3          
#      /      /                \     \                    \     \         
#     /      /                  \     \                    \     \        
#    4      5          ->        4     5          ->        4     5       
#   /      / \                  /     / \                  /     / \      
#  /      /   \                /     /   \                /     /   \     
# 6      7     8   [s]        6     7     8   [s]        6     7     8
#  \          / \            /           / \              \         / \   
#   \        /   \          /           /   \              \       /   \  
#    9      10   11        9           11   10              9     10   11 

## input
# 11
# 2 3
# 4 -1
# 5 -1
# 6 -1
# 7 8
# -1 9
# -1 -1
# 10 11
# -1 -1
# -1 -1
# -1 -1
# 2
# 2
# 4
## output
# 2 9 6 4 1 3 7 5 11 8 10
# 2 6 9 4 1 3 7 5 10 8 11