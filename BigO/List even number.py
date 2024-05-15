import sys

sys.setrecursionlimit(1000000000)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def postorder_traversal(root, even_numbers):
    if root:
        postorder_traversal(root.left, even_numbers)
        postorder_traversal(root.right, even_numbers)
        if root.value % 2 == 0:
            even_numbers.append(root.value)


n = int(input())
elements = list(map(int, input().split()))

bst_root = None
for element in elements:
    bst_root = insert(bst_root, element)

even_numbers = []
postorder_traversal(bst_root, even_numbers)

print(" ".join(map(str, even_numbers)))
