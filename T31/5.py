# Problem statement
# Given a singly linked list, you have to detect the loop and remove the loop from the linked list, if present. You have to make changes in the given linked list itself and return the updated linked list.

# Expected Complexity: Try doing it in O(n) time complexity and O(1) space complexity. Here, n is the number of nodes in the linked list.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def detect_loop(head):
    
    if not head:
        
        return None
    
    slow=head
    fast=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        
        if slow ==  fast:
            
            return True
        
    return False

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

# Set up the linked list nodes
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Create a loop: fifth node points back to third node
fifth.next = third 

print(detect_loop(head))