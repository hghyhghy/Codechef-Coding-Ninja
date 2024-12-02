# Problem statement
# You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.

# Note :
# Assume that the Indexing for the linked list always starts from 0.

# If the position is greater than or equal to the length of the linked list, you should return the same linked list without any change.
# Illustration :
# The following images depict how the deletion has been performed.
# Image-I :

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val= val
        self.next=next
        

def delete_with_position(head,pos):
    
    if not head:
        
        return None
    
    if pos == 0:
        
        return head.next
    
    current =head
    
    for _ in range(pos-1):
        
        if current and current.next:
        
            current =current.next
            
        else:
            
            return head
        
        
    if current.next is not None:
        
        current.next=current.next.next
        
    return head


def print_list(head):
    
    curr=head
    
    while curr:
        
        print(curr.val,end=" ")
        curr=curr.next
        
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original linked list:")
print_list(head)

# Delete node at position 2 (value 3)
head = delete_with_position(head, 2)

print("Linked list after deletion:")
print_list(head)