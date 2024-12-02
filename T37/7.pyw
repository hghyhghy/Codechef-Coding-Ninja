# Problem statement
# You are given the head node of a singly linked list 'head'. Your task is to modify the linked list in such a way that all the even valued nodes appear before the all odd valued node and order of nodes remain the same.



# Example :-
# The given singly linked list is  6 -> 5 -> 3 -> 4 -> 7 -> 1 -> 2 


class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def separate_even_and_odd(head):
    
    dummy_even=ListNode(0)
    dummy_odd=ListNode(0)

    even=dummy_even
    odd=dummy_odd
    
    current=head
    
    while current:
        
        if current.val % 2 ==0:
            
            even.next=current
            even=even.next
            
        else:
            
            odd.next=current
            odd=odd.next
            
        current=current.next
        
    odd.next=None
    
    even.next=dummy_odd.next
    
    return dummy_even.next

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val, end=" ")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)

print("Original List:")
print_list(head)

# Rearrange and print the modified list
modified_head = separate_even_and_odd(head)
print("Modified List:")
print_list(modified_head)