# Problem statement
# You are given the 'head' of a singly linked list. Your task is to group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list’s head.



# The first node is considered odd, and the second node is even, and so on.



# Note:
# Keep in mind that reordering is to be done according to the indexes and not the node values.
# # Also, ensure that the relative order inside both the even and odd groups should remain as it was in the input.

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def rearrange_odd_even(head):
    
    if not head:
        
        return None
    
    even=even_head=Node(0)
    odd=odd_head=Node(0)
    
    index=0
    current=head
    
    while current:
        
        if index%2 == 0:
            
            odd_head.next = current
            odd_head=odd_head.next
            
        else:
            
            even_head.next=current
            even_head =  even_head.next
            
        
        current=current.next
        
        index += 1
        
    
    odd_head.next= even.next
    even_head.next = None
    
    
    return odd.next

def print_list(head):
    
    curr=head
    
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
        
input_values = [1, 2, 3, 4, 5]
head = Node(input_values[0])
current = head
for value in input_values[1:]:
    current.next = Node(value)
    current = current.next

new_head = rearrange_odd_even(head)
print_list(new_head)