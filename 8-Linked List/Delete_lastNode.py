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



def Del_last(head):
    if head==None:
        return None
    if head.next==None:
        return None
    
    cur = head
    while cur.next.next!=None:
        cur=cur.next
    cur.next=None
    return head




head=Node(10)
head.next=Node(20)
head.next.next=Node(30)


head=Del_last(head)

printlist(head)