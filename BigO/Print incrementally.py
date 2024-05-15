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


def print_in_order(node):
    if node is not None:
        print_in_order(node.left)
        print(node.value, end=" ")
        print_in_order(node.right)


N = int(input())
numbers = list(map(int, input().split()))

bst_root = construct_bst(numbers)

print_in_order(bst_root)
