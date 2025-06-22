class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def printList(self):
        cur = self  # ✅ Start from 'self' instead of 'head'
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        #print()  # for clean output

    def search(self, n):
        cur = self  # ✅ Again, start from 'self'
        i = 1
        while cur:
            if cur.data == n:
                return i
            cur = cur.next
            i += 1
        return -1  # After loop if not found

# Create Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

head.printList()                 # Output: 10 20 15 30
print(head.search(40))           # Output: -1 (not found)
print(head.search(15))           # Output: 3  (found at position 3)
