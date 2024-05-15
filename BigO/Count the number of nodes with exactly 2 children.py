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


def count_nodes_with_two_children(node):
    if node is None:
        return 0
    count = 0
    if node.left is not None and node.right is not None:
        count = 1
    count += count_nodes_with_two_children(node.left)
    count += count_nodes_with_two_children(node.right)
    return count


N = int(input())
numbers = list(map(int, input().split()))

bst_root = construct_bst(numbers)
node_count = count_nodes_with_two_children(bst_root)

print(node_count)
