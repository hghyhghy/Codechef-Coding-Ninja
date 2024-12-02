# Problem statement
# Given a singly linked list of 'N' nodes. Your task is to delete the middle node of this list and return the head of the modified list.



# However, if the list has an even number of nodes, we delete the second middle node



# Example:
# If given linked list is 1->2->3->4 then it should be modified to 1->2->4.  


class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def delete_middle(head):
    
    if not head:
        
        return None
    
    prev=None
    slow=head
    fast=head
    
    while fast and fast.next:
        
        prev=slow
        slow=slow.next
        fast=fast.next.next
        
        
    if prev: 
        
        prev.next=slow.next
        
    return head

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original list:")
print_list(head)

# Delete the middle node
head = delete_middle(head)

print("Modified list after deleting middle node:")
print_list(head)
