

#odd even index element

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head):
    
    odd=head
    even=head.next
    even_head=even
    
    while even and even.next:
        
        odd.next=even.next
        odd=odd.next
        
        even.next=odd.next
        even=even.next
        
    odd.next=even_head
    
    return head


def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Rearrange linked list to odd-even: 1 -> 3 -> 5 -> 2 -> 4
new_head = main(head)
print_list(new_head) 
