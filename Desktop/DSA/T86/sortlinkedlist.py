# You are given a Singly Linked List of integers which is sorted based on absolute value.

# You have to sort the Linked List based on actual values.

# The absolute value of a real number x, denoted |x|, is the non-negative value of x without regard to its sign.

# Example:
# If the given list is {1 -> -2 -> 3} (which is sorted on absolute value), the returned list should be {-2 -> 1 -> 3}.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val =val
        self.next= next
        

def sort_list(head):
    
    stack=[]
    curr=head
    
    while curr:
        
        stack.append(curr.val)
        curr=curr.next
        
    
    stack.sort()
    
    sorted_head =  ListNode(stack[0]) if stack else None
    curr=sorted_head
    
    for val in stack[1:]:
        
        curr.next = ListNode(val)
        curr=curr.next
        
    
    return sorted_head

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
        
head = ListNode(1)
head.next = ListNode(-2)
head.next.next = ListNode(3)

print("Original List:")
print_list(head)

sorted_head = sort_list(head)

print("Sorted List by actual value:")
print_list(sorted_head)