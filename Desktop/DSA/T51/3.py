# Problem statement
# Given the head node of the singly linked list and an integer ‘k’, , find the value at the kth node from the end of the linked list.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def kth_node_from_linked_list(head,k):
    
    if not head:
        
        return
    
    fast=head
    slow=head
    
                    
    for _ in range(k):
        
        fast=fast.next
        
    while fast:
        
        slow=slow.next
        fast=fast.next
        
        
    return slow.val if slow else None

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Find the 2nd node from the end
k = 2
result = kth_node_from_linked_list(head, k)
print(result)