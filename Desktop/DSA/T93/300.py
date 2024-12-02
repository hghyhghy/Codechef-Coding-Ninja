

#addition of linked list 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def addition(l1,l2):
    
    dummy=ListNode()
    current=dummy
    
    carry =0
    while l1 or l1 or carry:
        
        v1=l1.val if l1 else 0
        v2=l2.val if l2 else 0
        
        total = v1+v2+carry
        
        carry=total //10
        reaminder=total % 10
        
        current.next=ListNode(reaminder)
        current=current.next
        
        if l1:
            l1=l1.next
            
        if l2:
            l2=l2.next
            
    return dummy.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Creating the second linked list: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Adding the two numbers
result = addition(l1, l2)

# Function to print the linked list
def print_linked_list(head: ListNode):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Printing the result linked list: should be 807 (7 -> 0 -> 8)
print_linked_list(result)
    
    