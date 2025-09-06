class ListNode:
    def __init__(self, val):
        self.val=val
        self.next=None


class Queue:
    # implementing this with Dummy Node
    def __init__(self):
        self.left=self.right=None

    def enqueue(self,val):
        newNode=ListNode(val)

        # If Queue is not Empty
        if self.right:
            self.right.next=newNode
            self.right=self.right.next
        
        # If Empty
        else:
            self.left=self.right=newNode

    
    def dequeue(self):
        # If queue is empty
        if self.left==None:
            return None
        
        value=self.left.val
        self.left=self.left.next
        if self.left==None:
            self.right=None
        return value
    

    def print(self):
        cur=self.left
        while cur:
            print(cur.val, end=" ")
            cur=cur.next
        print()




q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.print()         # 10 20 30
print(q.dequeue())  # 10
q.print()         # 20 30
