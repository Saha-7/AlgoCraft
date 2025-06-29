class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

def printList(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next



def insertEnd(head,value):
    if head==None:
        return Node(value)
    cur=head
    while(cur.next!=None):
        cur=cur.next
    cur.next=Node(value)
    return head


head=None
head=insertEnd(head,5)
head=insertEnd(head,10)

printList(head)