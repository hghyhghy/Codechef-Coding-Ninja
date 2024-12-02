
#add two list

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(l1,l2):
    
    dummy=ListNode(0)
    curr=dummy
    carry=0
    
    while l1 and l2:
        
        d1=l1.val if l1 else 0
        d2=l2.val if l2 else 0
        
        total=d1+d2+carry
        carry = total // 10
        remainder=total % 10
        
        curr.next=ListNode(remainder)
        curr=curr.next
        
        if l1:
            
            l1=l1.next
            
        if l2:
            
            l2=l2.next
            
    return dummy.next

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
l1 = ListNode(2, ListNode(4, ListNode(3)))
# List 2: 5 -> 6 -> 4 (represents 465)
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Add the two numbers
result = main(l1, l2)

print_list(result)