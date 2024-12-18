# Problem statement
# You are given a Singly Linked List of integers. You have to return true if the linked list is palindrome, else return false.



# A Linked List is a palindrome if it reads the same from left to right and from right to left.



# Example:
# The lists (1 -> 2 -> 1), (3 -> 4 -> 4-> 3), and (1) are palindromes, while the lists (1 -> 2 -> 3) and (3 -> 4) are not.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def check_palindrome(head):
    
    if not head:
        
        return
    
    stack=[]
    current=head
    
    while current:
        
        stack.append(current.val)
        current=current.next
        
    
    current=head
    
    while current:
        
        if stack.pop() != current.val:
            
            return False
        
        current=current.next
        
    return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

print(check_palindrome(head))