
class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next


def main(head,k):
    
    dummy=ListNode(0)
    dummy.next=head
    fast=dummy
    slow=dummy
    
    for _ in range(k):
        
        fast=fast.next
        
    while fast.next:
        
        slow=slow.next
        fast=fast.next
        
    slow.next=slow.next.next
    
    return dummy.next

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end="->")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
print_list(head)

# Remove the 2nd node from the end
head = main(head, 2)

print("List after removing 2nd node from the end:")
print_list(head)