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


def inorder_traversal(root, x, sum_nodes):
    if root:
        inorder_traversal(root.left, x, sum_nodes)
        if root.value < x:
            sum_nodes[0] += root.value
        inorder_traversal(root.right, x, sum_nodes)


n, x = map(int, input().split())
numbers = list(map(int, input().split()))

bst_root = None
for number in numbers:
    bst_root = insert(bst_root, number)

sum_nodes = [0]
inorder_traversal(bst_root, x, sum_nodes)

print(sum_nodes[0])
