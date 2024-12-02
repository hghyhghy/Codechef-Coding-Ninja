
#cycle detection in a linked list

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(head):
    
    if not head:
        return None
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        if slow == fast:
            
            return True
        
    return False

if __name__ == "__main__":
    # Create nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    # Link nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create a cycle for testing

    # Check for cycle
    result = main(node1)
    print(result)  #