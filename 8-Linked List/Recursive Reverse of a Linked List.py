class Node:
    def __init__(self, k):
        self.data = k
        self.next = None


    ## Normal Approach ##
# def reverseList(head):
#    stack=[]
#    cur=head

#    while cur:
#        stack.append(cur.data)
#        cur=cur.next
    
#    curr=head
#    while curr:
#        curr.data=stack.pop()
#        curr=curr.next
    
#    return head

# 1->2->3->None
# nextNode=2
# 1.next=None
# prev=10
# cur=20
# 1=> 

def reverseList(head,prev=None):
    if head==None:
        return prev
    
    cur=head
    nextNode=cur.next
    cur.next=prev
    prev=cur
    return reverseList(nextNode,cur)
      

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

head = reverseList(head)

printList(head)
