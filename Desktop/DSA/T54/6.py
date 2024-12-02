# Problem statement
# Given the head node of the singly linked list and an integer ‘k’, , find the value at the kth node from the end of the linked list.

# For example:

# For the above-linked list, if k=2, then the value at the kth i.e second node from the end is ‘12’.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def kth_node_from_list(head,k):
    
    if not head:
        
        return None
    
    fast=head
    slow=head
    
    for _ in range(k):
        
        fast=fast.next
        
    while fast:
        
        slow=slow.next
        fast=fast.next
        
    return slow

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val, end=" ")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
result_node = kth_node_from_list(head, k)
if result_node:
    print(f"The {k}-th node from the end is {result_node.val}")
else:
    print(f"There is no {k}-th node from the end in the list")
        