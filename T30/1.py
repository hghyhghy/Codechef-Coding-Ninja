# Problem statement
# Given a singly linked list of 'N' nodes. The objective is to determine the middle node of a singly linked list. However, if the list has an even number of nodes, we return the second middle node.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def middle_of_the_linked_list(head):
    
    if head is None:
        
        return None
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
    return slow

def print_middle(middle_node):
    if middle_node:
        print(f"Middle Node Value: {middle_node.val}")
    else:
        print("The list is empty")
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

middle = middle_of_the_linked_list(head)
print_middle(middle)
    