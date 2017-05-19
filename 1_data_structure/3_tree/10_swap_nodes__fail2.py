
import queue

LEFT = 0
RIGHT = 1

class Node:
    def __init__(self, data=None, height=0, left=None, right=None):
        self.data = data
        self.height = height
        self.left = left
        self.right = right


N = int(input())
height = 0
root = Node(1, 1, None, None)
q = queue.Queue()
q.put(root)
node_cnt = 1
for i in range(N):
    a, b = map(int, input().split(' '))

    node = q.get()

    if a != -1:
        node.left = Node(a, height+2)
        q.put(node.left)

    if b != -1:
        node.right = Node(b, height+2)
        q.put(node.right)

    if node_cnt == 2**height:
        height += 1
        node_cnt = 1
    else:
        node_cnt += 1


K = int(input())
depths = []
for _ in range(K):
    depths.append(int(input()))

def swap_node(root, pt, pts):
    if root:
        if root.height >= pt and root.height not in pts:
            root.left, root.right = root.right, root.left

        swap_node(root.left, pt, pts)
        print(root.data, end=' ')
        swap_node(root.right, pt, pts)

        return root

for _ in range(K):
    root = swap_node(root, depths[0], depths)
    depths.remove(depths[0])
    print()