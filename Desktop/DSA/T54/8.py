# Given two numbers represented by two linked lists, the task is to write a function that returns the sum of the two linked lists in the form of a list.

# Note: It is not allowed to modify the lists. Also, not allowed to use explicit extra space (Hint: Use Recursion).

# Example :

# Input: First List: 5->6->3, Second List: 8->4->2 
# Output: Resultant list: 1->4->0->5
# Explanation: Sum of 563 and 842 is 1405



class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def add_two_list(l1,l2):

    dummy=ListNode(0)
    current=dummy
    carry =0
    
    while l1 or l2:
        
        val1=l1.val if l1 else 0
        val2=l2.val if l2 else 0
        
        total=val1+val2+carry
        carry = total // 10
        remainder= total%10
        
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
        
        print(curr.val , end=" ")
        curr=curr.next
        
l1 = ListNode(2, ListNode(4, ListNode(3)))
# List 2: 5 -> 6 -> 4 (represents 465)
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Add the two numbers
result = add_two_list(l1, l2)

print_list(result)

    
    