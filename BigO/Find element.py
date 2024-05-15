class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_position(head, x):
    position = 1
    current = head

    while current is not None:
        if current.data == x:
            return position
        elif current.data > x:
            return -1

        current = current.next
        position += 1

    return -1

N, x = map(int, input().split())

arr = list(map(int, input().split()))
head = None
prev = None
for i in range(N):
    node = Node(arr[i])
    if prev is not None:
        prev.next = node
    else:
        head = node
    prev = node

position = find_position(head, x)

print(position)