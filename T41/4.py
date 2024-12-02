# Problem statement
# Ninjas is practicing problems on the linked list. He came across a problem in which he has given a linked list of ‘N’ nodes and two integers, ‘LOW’ and ‘HIGH’. He has to return the linked list ‘HEAD’ after reversing the nodes between ‘LOW’ and ‘HIGH’, including the nodes at positions ‘LOW’ and ‘HIGH’.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def reverse_linked_list(head):
    
    if head is None:
        
        return None
    
    prev=None
    curr=head 
    
    while curr:
        
        node=curr.next
        curr.next=prev
        prev=curr
        curr=node
        
    return prev 

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original Linked List:")
print_list(head)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

print("Reversed Linked List:")
print_list(reversed_head)