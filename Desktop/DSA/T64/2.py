# Problem statement
# You are given a Singly Linked List of integers with a head pointer. Every node of the Linked List has a value written on it.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def check(head,target):
    
    if not head or not target:
        
        return False
    
    current = head
    
    while current:
        
        if current.val == target:
            
            return True
        
        current=current.next
        
    return False

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(check(head,3))