# Problem statement
# Given a singly linked list of 'N' nodes. The objective is to determine the middle node of a singly linked list. However, if the list has an even number of nodes, we return the second middle node.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def finding_middle(head):
    
    if not head:
        
        return None
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
    return slow

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle = finding_middle(head)

# Print the value of the middle node, if it exists
if middle:
    print(f"The middle node's value is: {middle.val}")
else:
    print("The list is empty")