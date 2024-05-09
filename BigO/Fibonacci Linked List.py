class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result


def fib_linked_list(x, y, n):
    linked_list = LinkedList()

    linked_list.append(x)
    linked_list.append(y)

    current = linked_list.head

    for _ in range(n - 2):
        next_data = (current.data + current.next.data) % (10**6 + 7)
        new_node = Node(next_data)
        current.next.next = new_node
        current = current.next

    return linked_list.to_list()


x, y, n = map(int, input().split())

result = fib_linked_list(x, y, n)

print(*result)
