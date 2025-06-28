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


def insert_at_X(head,data,pos):
    temp=Node(data)
    if pos==1:
        temp.next=head
        return temp
    
    cur=head
    for i in range(pos-2):
        if cur==None:
            return head
        cur=cur.next
    temp.next=cur.next
    cur.next=temp
    return head
    








head=None
head=insert_at_X(head,5,1)
head=insert_at_X(head,10,2)
head=insert_at_X(head,20,3)
head=insert_at_X(head,30,4)

head=insert_at_X(head,15,3)


printlist(head)