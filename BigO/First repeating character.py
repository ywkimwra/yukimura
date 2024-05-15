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

    def contains(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


def find_first_repeating_character(string):
    linked_list = LinkedList()

    for char in string:
        if linked_list.contains(char):
            return char

        linked_list.append(char)

    return None


string = input()
result = find_first_repeating_character(string)

print(result if result is not None else "null")
