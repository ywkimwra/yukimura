import sys

sys.setrecursionlimit(1000000000)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct_bst(nums):
    def construct(node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = construct(node.left, value)
        else:
            node.right = construct(node.right, value)
        return node

    root = None
    for num in nums:
        root = construct(root, num)
    return root


def calculate_leaf_sum(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.value
    left_sum = calculate_leaf_sum(node.left)
    right_sum = calculate_leaf_sum(node.right)
    return left_sum + right_sum


N = int(input())
numbers = list(map(int, input().split()))

bst_root = construct_bst(numbers)
leaf_sum = calculate_leaf_sum(bst_root)

print(leaf_sum)
