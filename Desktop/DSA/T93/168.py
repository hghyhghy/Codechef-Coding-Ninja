

#add linked list

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(l1,l2):
    
    dummy =ListNode(0)
    curr=dummy
    carry = 0
    
    while l1 or l2 or carry:
        
        d1=l1.val if l1 else 0
        d2=l2.val if l2 else 0
        
        total =  d1+d2+carry
        carry = total // 10
        remainder=  total % 10
        
        curr.next = ListNode(remainder)
        curr=curr.next
        
        
        if l1:
            
            l1=l1.next
            
        if l2:
            
            l2=l2.next
            
            
    return dummy.next

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val, end=" ")
        curr=curr.next
        
num1 = ListNode(2)
num1.next = ListNode(4)
num1.next.next = ListNode(3)

# num2 = [5, 6, 4] which represents the number 465
num2 = ListNode(5)
num2.next = ListNode(6)
num2.next.next = ListNode(4)

result = main(num1, num2)

print_list(result)