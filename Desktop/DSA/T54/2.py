# Problem statement
# You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.

# Note :
# Assume that the Indexing for the linked list always starts from 0.

# If the position is greater than or equal to the length of the linked list, you should return the same linked list without any change.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def delete_node(head,target):
    
    if not head:
        
        return None
    
    if head.val == target:
        
        return head.next
    
    current=head
    
    while current.next:
        
        if current.next.val ==  target:
            
            current.next=current.next.next
            
        current=current.next
        
    return head 

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end="->")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
print_list(head)

# Delete node with value 3
head = delete_node(head, 3)

print("List after deleting node with value 3:")
print_list(head)
            
            