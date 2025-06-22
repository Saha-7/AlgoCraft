class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

def printList(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next

def AddFront(head,x):
    newNode=Node(x)
    newNode.next=head
    return newNode


head=None
head=AddFront(head,15)
head=AddFront(head,20)
head=AddFront(head,25)


printList(head)