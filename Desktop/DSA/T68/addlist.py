# Problem statement
# You are given two non-negative numbers 'num1' and 'num2' represented in the form of linked lists.



# The digits in the linked lists are stored in reverse order, i.e. starting from least significant digit (LSD) to the most significant digit (MSD), and each of their nodes contains a single digit.



# Calculate the sum of the two numbers and return the head of the sum list.

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def add_list(l1,l2):
    
    dummy =Node()
    curr=dummy
    carry =0 
    
    
    while l1 or l2 or carry:
        
        v1=l1.val if l1 else 0
        v2=l2.val if l2 else 0
        
        total= v1+v2+carry
        
        carry = total //10
        remainder=total % 10
        
        curr.next=Node(remainder)
        curr=curr.next
        
        
        if l1:
            
            l1=l1.next
            
        if l2:
            
            l2=l2.next
            
            
    return dummy.next

def printList(head):
    
    curr=head
    
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        



head1 = Node(2, Node(4, Node(3)))
# num2 = 465 (represented as 5 -> 6 -> 4)
head2 = Node(5, Node(6, Node(4)))

# Add two numbers
result = add_list(head1, head2)

# Output result list
printList(result)