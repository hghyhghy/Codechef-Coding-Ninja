# Problem statement
# You are given two non-negative numbers 'num1' and 'num2' represented in the form of linked lists.



# The digits in the linked lists are stored in reverse order, i.e. starting from least significant digit (LSD) to the most significant digit (MSD), and each of their nodes contains a single digit.



# Calculate the sum of the two numbers and return the head of the sum list.

class ListNode:
    
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
def add_linked_list(l1,l2):
    
    if not l1 and not l2:
        
        return None
    
    dummy=ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        
        digit1 =  l1.val if l1 else 0
        digit2=   l2.val if l2 else 0
        
        total =  digit1+digit2+carry
        carry = total // 10
        remainder= total % 10
        
        current.next = ListNode(remainder)
        current=current.next
        
        
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

result = add_linked_list(num1, num2)

print_list(result)  # Output should be: 7 -> 0 -> 8
