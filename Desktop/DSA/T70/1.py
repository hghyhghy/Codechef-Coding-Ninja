# Problem statement
# Given the head node of the singly linked list and an integer ‘k’, , find the value at the kth node from the end of the linked list.

# For example:

# For the above-linked list, if k=2, then the value at the kth i.e second node from the end is ‘12’.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def kth_element(head,k):
    
    if not head or not k:
        
        return None
    
    fast=head
    slow=head
    
    for _ in range(k):
        
        if fast is None:
            
            return None
        
        fast=fast.next
        
    while fast:
        
        slow=slow.next
        fast=fast.next
        
    return slow.val if slow else None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
result = kth_element(head, k)
print(result)  # Output: 4