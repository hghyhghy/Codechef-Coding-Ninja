# 141. Linked List Cycle
# Easy
# Topics
# Companies
# Given head, the head of a linked list, determine if the linked list has a cycle in it.


class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def detecting_cycle(head):
    
    if not head:
        
        return None
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        
        if slow ==  fast:
            
            return True

    return False

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

print(detecting_cycle(head))