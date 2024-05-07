class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if self.head is not None:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next


n = int(input())
linked_list = LinkedList()

for _ in range(n):
    query = input().split()
    if query[0] == "0":
        linked_list.remove_head()
    elif query[0] == "1":
        x = int(query[1])
        linked_list.add_node(x)

linked_list.print_list()
