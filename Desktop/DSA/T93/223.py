

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

        if fast == slow:
            
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

print(main(node1))
        
        
        