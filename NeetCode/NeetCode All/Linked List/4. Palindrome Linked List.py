# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        # reverse the 2nd half
        prev=None
        while slow:
            nextNode=slow.next
            slow.next=prev
            prev=slow
            slow=nextNode
        

        # comparng left to right
        left, right = head, prev
        while right:
            if left.val !=right.val:
                return False
            left=left.next
            right=right.next
        return True
