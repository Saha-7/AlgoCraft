class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Outsider Function
def printList(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next


head = Node(10)
head.next = Node(20)               # 2nd node
head.next.next = Node(15)          # 3rd node
head.next.next.next = Node(30)     # 4th node — safe now!

printList(head)
