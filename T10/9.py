# Remove N-th node from back of LinkedList

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def deleting_node(head:ListNode,n:int) -> ListNode:
    
    if not head:
        
        return None
    
    dummy=ListNode(0,head)

    fast=dummy
    slow=dummy
    
    for _ in range(n+1):
        
        fast=fast.next
        
    while fast:
        
        fast=fast.next
        slow=slow.next
        
    slow.next=slow.next.next
    
    return dummy.next


def print_list(head:ListNode):
    
    curr=head
    while curr:
        
        print(curr.val, end=" ")
        curr=curr.next
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original list:")
print_list(head)

# Delete the 2nd node from the end (which is 4)
n = 2
head = deleting_node(head, n)

print(f"List after deleting the {n}th node from the end:")
print_list(head)