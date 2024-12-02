# sum of the elements of the linked list

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def sum_elements(l1,l2):
    

    
    dummy=ListNode(0)
    current=dummy
    
    carry  = 0
    
    while l1 or l2 or carry:
        
        digit1= l1.val if l1 else 0
        digit2= l2.val if l2 else 0
        
        total= digit1+digit2+carry
        
        carry =  total // 10
        
        current.next= ListNode(total%10)
        
        current=current.next
        
        if l1:
            
            l1=l1.next
            
        if l2:
            
            l2=l2.next
            
    return dummy.next
    
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = sum_elements(l1, l2)

# Printing the result: Should be 7 -> 0 -> 8, representing 807
while result:
    print(result.val, end="" if result.next else "")
    result = result.next