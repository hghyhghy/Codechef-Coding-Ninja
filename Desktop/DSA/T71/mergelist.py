#  Merge Two Sorted Linked Lists
# Moderate
# 0/80
# Average time to solve is 15m
# 294 upvotes
# Asked in companies
# Problem statement
# You are given two sorted linked lists. You have to merge them to produce a combined sorted linked list. You need to return the head of the final linked list.

# Note:

# The given linked lists may or may not be null.
# For example:

# If the first list is: 1 -> 4 -> 5 -> NULL and the second list is: 2 -> 3 -> 5 -> NULL

# The final list would be: 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> NULL

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def merge_list(l1,l2):
    
    dummy=Node(0)
    curr=dummy
    
    p1=l1
    p2=l2
    
    while p1 and  p2:
        
        if p1.val<p2.val:
            
            curr.next=p1
            p1=p1.next
            
            
        else:
            
            curr.next=p2
            p2=p2.next
        
        curr=curr.next
        
    return dummy.next

def printList(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
head1 = Node(1)
head1.next = Node(4)
head1.next.next = Node(5)

# Creating the second linked list: 2 -> 3 -> 5 -> NULL
head2 = Node(2)
head2.next = Node(3)
head2.next.next = Node(5)

print("First List:")
printList(head1)

print("Second List:")
printList(head2)

# Merging the two lists
merged_head = merge_list(head1, head2)

print("Merged List:")
printList(merged_head)