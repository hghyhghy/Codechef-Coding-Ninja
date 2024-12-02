# detecting cycle in the linked list

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def detecting_cycle(head):
    
    if not head or not head.next:
        
        return False
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        
        if slow == fast:
            
            return True
        
    
    return False

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(detecting_cycle(node1))
    