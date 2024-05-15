class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_new_linked_list(head):
    if not head or not head.next:
        return head

    new_head = ListNode(head.val)
    new_current = new_head
    current = head.next

    while current:
        new_val = current.val + current.prev.val
        new_node = ListNode(new_val)
        new_current.next = new_node
        new_current = new_node

        current.prev = current
        current = current.next

    return new_head

n = int(input())
elements = list(map(int, input().split()))

head = ListNode(elements[0])
current = head
for i in range(1, n):
    node = ListNode(elements[i])
    current.next = node
    node.prev = current
    current = node

new_head = build_new_linked_list(head)

while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next