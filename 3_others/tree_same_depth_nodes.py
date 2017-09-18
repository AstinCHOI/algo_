#!/usr/bin/python3


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)
j = Node(10)
k = Node(11)

root = a
root.left = b
root.right = c

b.left = d
b.right = e
c.left = f
c.right = g

d.left = h
d.right = i


def get_height(root, height, value):
    if root.value == value:
        return height

    if root.left:
        return get_height(root.left, height+1, value)

    if root.right:
        return get_height(root.right, height+1, value)

    return height-1


def get_same_height_node(root, height, same):
    if height == same:
        print(root.value)
        return

    if root.left:
        get_same_height_node(root.left, height+1, same)

    if root.right:
        get_same_height_node(root.right, height+1, same)


# print(get_height(root, 1, 6))

same = get_height(root, 1, 6)
get_same_height_node(root, 1, 4)