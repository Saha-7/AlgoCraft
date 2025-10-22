# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        if head==None:
            return

        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
    

head=ListNode(10)
head.next=ListNode(20)
head.next.next=ListNode(30)

ans=Solution()

print(ans.middleNode(head))

print(ans.middleNode(head).val)
