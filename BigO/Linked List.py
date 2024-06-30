class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(value):
    head = None
    cur = None

    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
            curr = new_node
        else:
            cur.next = new_node
            cur = new_node
    return head

def find_intersection(head1, head2):
    if not head1 or not head2:
        return None
    
    value1 = []
    cur1 = head1
    while cur1:
        value1.append(cur1.data)
        cur1 = cur1.next

    value2 = []
    cur2 = head2
    while cur2:
        value2.append(cur2.data)
        cur2 = cur2.next

    intersection = [value for value in value1 if value in value2]

    head = None
    cur = None
    for value in intersection:
        new_node = Node(value)
        if head is None:
            head = new_node
            cur = new_node
        else:
            cur.next = new_node
            cur = new_node
    return head

list1 = []
list2 = []

while True:
    x = int(input())
    if x == -1:
        break
    list1.append(x)

while True:
    x = int(input())
    if x == -1:
        break
    list2.append(x)

head1 = create_linked_list(list1)
head2 = create_linked_list(list2)

intersection = find_intersection(head1, head2)

if intersection is None:
    print("NO INTERSECTION")
else:
    cur = intersection
    while cur:
        print(cur.data, end=" ")
        cur = cur.next