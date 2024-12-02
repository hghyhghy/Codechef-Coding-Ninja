# You are given a singly Linked List of integers. Your task is to return true if the given singly linked list is a palindrome otherwise returns false.

# For example:
# The given linked list is 1 -> 2 -> 3 -> 2-> 1-> NULL.

# It is a palindrome linked list because the given linked list has the same order of elements when traversed forwards and backward​.
# Follow Up:
# Can you solve the problem in O(N) time complexity and O(1) space complexity iteratively?

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def palindrome_list(head):
    
    if not head:
        
        return None
    
    stack=[]
    curr=head
    
    while curr:
        
        stack.append(curr.val)
        curr=curr.next
        
    curr=head
    
    while curr:
        
        new=stack.pop()
        if new != curr.val:
            
            return False
        
        curr=curr.next
        
    return True

print(palindrome_list())