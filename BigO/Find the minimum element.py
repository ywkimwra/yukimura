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


def find_smallest_element(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.value


N = int(input())
numbers = list(map(int, input().split()))

bst_root = construct_bst(numbers)
smallest = find_smallest_element(bst_root)

print(smallest)
