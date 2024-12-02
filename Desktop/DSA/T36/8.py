# Problem statement
# You are given a Singly Linked List of integers with a head pointer. Every node of the Linked List has a value written on it.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def search_in_the_linked_list(head,target):
    
    if not head:
        
        return None
    
    current=head
    
    while current:
        
        if current.val ==  target:
            
            return True
        
        current=current.next
        
    return False

def print_list(head):
    
    current=head
    while current:
        
        print(current.val, end=" ")
        current=current.next
        
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(search_in_the_linked_list(head,3))
    