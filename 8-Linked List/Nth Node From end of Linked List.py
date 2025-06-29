class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


    ## Method 1(Using length of Linked List) ##

# def printNthFromEnd(head,n):
#     if head==None:
#         return
#     cur=head
#     count=0
#     while cur:
#         cur=cur.next
#         count+=1

#     cur=head
#     if count<n:
#         return

#     for i in range(count-n):
#         cur=cur.next
#     print(cur.data)





    ## Using Two pointer Approach ##

def printNthFromEnd(head,n):
    if head==None:
        return
    slow=



    
            
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(40)



printList(head)
printNthFromEnd(head,2)
