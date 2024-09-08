# Problem statement
# You are given a Singly Linked List of integers. You need to reverse the Linked List by changing the links between nodes

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def reverse_linked_list(head):
    
    curr =head
    prev=None
    
    while curr is not None:
        
        node=curr.next
        curr.next=prev
        prev=curr
        curr=node
        
    head=prev
    return head

def print_list(head):
    
    current=head
    while current:
        
        print(current.val, end=" ")
        current = current.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reversed_head = reverse_linked_list(head)
print_list(reversed_head)