# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        cur = node

        
        cur.val=cur.next.val
        cur.next=cur.next.next
        
        
        
# Helper function to print linked list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

# Create linked list: 10 -> 20 -> 30 -> 40
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)

print("Original list:")
printList(head)

# Delete node with value 20
node_to_delete = head.next  # Node with value 20
sol = Solution()
sol.deleteNode(node_to_delete)

print("List after deleting node 20:")
printList(head)