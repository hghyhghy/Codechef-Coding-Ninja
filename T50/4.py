# llinked list reversal 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def reversal(head):
    
    if not head:
        
        return None
    
    current = head
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
        
        print(curr.val , end=" ")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
print_list(head)

# Reverse the linked list
reversed_head = reversal(head)

print("Reversed linked list:")
print_list(reversed_head)