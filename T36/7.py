# reverse the linked list

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def reverse_list(head):
    
    if not head:
        
        return None
    
    current=head
    prev=None
    
    while current:
        
        node=current.next
        current.next=prev
        prev=current
        current=node
        
    return prev

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val, end=" ")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original List:")
print_list(head)

# Reversing the linked list
reversed_head = reverse_list(head)

print("Reversed List:")
print_list(reversed_head)
