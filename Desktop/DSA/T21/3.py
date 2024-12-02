# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def add_two_linked_list_element(l1,l2):
    
    dummy=ListNode()
    current = dummy
    
    carry = 0
    
    while l1 or l2 or carry:
        
        val1=l1.val if l1 else 0
        val2=l2.val if l2 else 0

        total_digit= val1 +val2+ carry
        
        carry =total_digit//10
        
        new_digit = total_digit%10
        
        current.next = ListNode(new_digit)
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
result = add_two_linked_list_element(l1, l2)

# Function to print the linked list
def print_linked_list(head: ListNode):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Printing the result linked list: should be 807 (7 -> 0 -> 8)
print_linked_list(result)