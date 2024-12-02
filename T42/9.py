# cycle detection in the singly linked  list 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next


def cycle_detection(head):
    
    if not head:
        
        return None
    
    slow=head
    fast=head
    
    while fast and  fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        if slow ==  fast:
            
            return True
    
    return False

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2 

print(cycle_detection(node1))