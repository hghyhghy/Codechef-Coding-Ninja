

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def reverse_main(head):
    
    curr=head
    prev=None
    
    while curr:
        
        node=curr.next
        curr.next=prev
        prev=curr
        curr=node
        
    return prev 

def main(l1,l2):
    
    dummy=ListNode(0)
    l1=reverse_main(l1)
    l2=reverse_main(l2)

    carry=0
    curr=dummy
    
    while l1 or l2 or carry:
        
        d1=l1.val if l1 else 0
        d2=l2.val if l2 else 0
        
        total =  d1+d2+carry
        carry = total // 10
        
        curr.next=ListNode(total%10)
        curr=curr.next
        
        if l1:
            l1=l1.next
            
        if l2:
            
            l2=l2.next
            
    store=reverse_main(dummy.next)
    return store

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()  # for new line

# Example usage
l1 = ListNode(2, ListNode(4, ListNode(3)))  # represents number 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # represents number 465

result = main(l1, l2)
print_list(result)