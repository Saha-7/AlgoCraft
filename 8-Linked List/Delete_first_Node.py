class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    

def printlist(head):
    cur=head
    while cur:
        print(cur.data, end=" ")
        cur=cur.next
    print()

def Delete_first(head):
    if head==None:
        return None
    else:
        return head.next



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)


head=Delete_first(head)

printlist(head)

