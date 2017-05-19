
# Worst and timeout problem

import queue

LEFT = 0
RIGHT = 1

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data, end=' ')
        Inorder(root.right)


N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split(' '))
    arr.append([a, b])

K = int(input())
depths = []
for j in range(K):
    depths.append(int(input()))

temp_arr = []
new_arr = []
## Make arranged array
## Start from the child of root (so height starts from 2)
root = Node(1)
height = 0
node_cnt = 1
for depth in depths:
    for i in range(N):
        if ((height+2) > depth) and ((height+2) not in depths):
            arr[i][LEFT], arr[i][RIGHT] = arr[i][RIGHT], arr[i][LEFT]

        temp_arr.append(arr[i])

        if node_cnt == 2**height:
            height += 1
            node_cnt = 1
            while(temp_arr):
                new_arr.append(temp_arr.pop())

        else:
            node_cnt += 1

    arr = new_arr
    height = 0
    node_cnt = 1
    q = queue.Queue()
    q.put(root)

    for item in arr:
        node = q.get()

        if item[LEFT] != -1:
            node.left = Node(item[LEFT])
            q.put(node.left)

        if item[RIGHT] != -1:
            node.right = Node(item[RIGHT])
            q.put(node.right)

    Inorder(root)
    print()