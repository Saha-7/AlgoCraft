class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

Head = Node(10)
Head.next=Node(20)
Head.next.next=Node(30)



print(Head.data)
print(Head.next)