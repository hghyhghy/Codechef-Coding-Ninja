

#middle of the list 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(head):
    
    if not head:
        
        return  None
    
    slow=head
    fast=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        return slow
    

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle  =main(head)
if middle:
    print(f"The middle element is: {middle.val}")
else:
    print("The linked list is empty.")