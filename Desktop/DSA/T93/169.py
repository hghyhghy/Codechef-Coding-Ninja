

#detect cycle 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head):
    
    fast=head
    slow=head

    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        if slow == fast:
            
            return True
        
    return False

node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
node3.next = node1  # Creates a cycle

print(main(node1))
    