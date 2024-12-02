# Problem statement
# You are given a Singly Linked List of integers. Return true if it has a cycle, else return false.



# A cycle occurs when a node's next points back to a previous node in the list.



# Example:
# In the given linked list, there is a cycle, hence we return true.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def cycle_detect(head):

    if not head:
        
        return None
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            
            return True
        
    return None

node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
node3.next = node1  # Creates a cycle

print(cycle_detect(node1))
    