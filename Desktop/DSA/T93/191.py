
#finding middle 
class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(head):
    
    slow=head
    fast=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
    return slow

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle = main(head)

# Print the value of the middle node, if it exists
if middle:
    print(f"The middle node's value is: {middle.val}")
else:
    print("The list is empty")