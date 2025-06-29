
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


    
def printMiddle(head):
  ## Naive Approach (traversing twice) ##
  
    # if head == None:
    #     return
    # count = 0 
    # curr = head
    # while curr :
    #     curr = curr.next
    #     count+=1
    
    # curr = head
    # for i in range (count//2):
    #     curr = curr.next
    # print(curr.data)



   ## Efficient Approach (Slow-Fast Pointer) ## 

    if head==None:
        return
    
    slow=head
    fast=head

    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next

    print(slow.data)
    
            
    
    
    
        

head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
printMiddle(head)
