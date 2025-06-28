class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

def printList(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next


def insert_in_Sorted(head,x):
    temp=Node(x)

    if head==None:
        return temp
    
    elif head.data>x:
        temp.next=head
        return temp
    
    else:
        cur=head
        while cur.next!=None and cur.next.data<x:
            cur=cur.next
        
        temp.next=cur.next
        cur.next=temp
        return head



# Create an empty list
head = None

# Insert values one by one into the sorted list
for value in [10, 20, 30, 40, 25, 5, 50]:
    head = insert_in_Sorted(head, value)

# Print the final sorted list
print("Final sorted linked list:")
printList(head)
