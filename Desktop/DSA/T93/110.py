

#reverse linked list
class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def main(head):
    
    if not head:
        
        return None
    
    curr=head
    prev=None
    
    while curr:
        
        node=curr.next
        curr.next=prev
        prev=curr
        curr=node
        
    return prev

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
print_list(head)

reversed_head = main(head)

print("\nReversed Linked List:")
print_list(reversed_head)