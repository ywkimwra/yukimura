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


def calculate_height(node):
    if node is None:
        return 0
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    return max(left_height, right_height) + 1


N = int(input())
numbers = list(map(int, input().split()))

bst_root = construct_bst(numbers)
height = calculate_height(bst_root)

print(height)
