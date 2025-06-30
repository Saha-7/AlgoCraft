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


    
def removeDup(head):
    cur=head
    while cur!=None and cur.next!=None:
        if cur.data==cur.next.data:
            cur.next=cur.next.next
        else:
            cur=cur.next
    
    
    
        

head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
removeDup(head)
printList(head)
