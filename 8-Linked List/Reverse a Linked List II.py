# NeetCode.io
class ListNode:
    def __init__(self, val, next=None):
        self.val = val  # Fixed: should be self.val, not self.value
        self.next = next

    def printList(self, head):
        cur = head
        while cur != None:
            print(cur.val, end=" ")  # Fixed: use self.val
            cur = cur.next
        print()

    def reverse_II(self, head, left, right):
        dummy = ListNode(-1, head)
        leftPrev = dummy
        cur = head

        for i in range(left - 1):
            cur = cur.next
            leftPrev = leftPrev.next  # Fixed: should be leftPrev.next, not cur

        prev = None
        for i in range(right - left + 1):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next


# Driver code
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
head.printList(head)

# Reverse from position 2 to 4
new_head = head.reverse_II(head, 2, 4)  # Fixed: call method on instance

print("After reversing from position 2 to 4:")
new_head.printList(new_head)  # Fixed: pass new_head as argument









## printList & reverse_II is stand alone functions here ##

# NeetCode.io
# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


# def printList(head):
#     cur = head
#     while cur != None:
#         print(cur.val, end=" ")
#         cur = cur.next
#     print()


# def reverse_II(head, left, right):
#     dummy = ListNode(-1, head)
#     leftPrev = dummy
#     cur = head

#     for i in range(left - 1):
#         cur = cur.next
#         leftPrev = leftPrev.next

#     prev = None
#     for i in range(right - left + 1):
#         nextNode = cur.next
#         cur.next = prev
#         prev = cur
#         cur = nextNode

#     leftPrev.next.next = cur
#     leftPrev.next = prev

#     return dummy.next


# # Driver code
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

# print("Original List:")
# printList(head)

# # Reverse from position 2 to 4
# new_head = reverse_II(head, 2, 4)

# print("After reversing from position 2 to 4:")
# printList(new_head)