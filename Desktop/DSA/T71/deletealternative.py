# Problem statement
# Given a Singly Linked List of integers, delete all the alternate nodes in the list.

# Example:
# List: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> null
# Alternate nodes will be:  20, 40, and 60.

# Hence after deleting, the list will be:
# Output: 10 -> 30 -> 50 -> null
# Note :
# The head of the list will remain the same. Don't need to print or return anything.

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def delete_alternative(head):
    
    if not head:
        
        return None
    
    curr=head
    while curr and curr.next:
        
        new=curr.next
        curr.next=new.next
        curr=curr.next
        
def printList(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

print("Original List:")
printList(head)

# Deleting alternate nodes
delete_alternative(head)

print("\nList after deleting alternate nodes:")
printList(head)