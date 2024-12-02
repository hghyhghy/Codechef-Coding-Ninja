# Problem statement
# For a given Singly Linked List of integers, sort the list using the 'Merge Sort' algorithm.

# Detailed explanation ( Input/output format, Notes, Images )

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def merge_linked_list(l1,l2):
    
    dummy=ListNode()
    current=dummy
    
    while l1 and l2:
        
        if l1.val <= l2.val:

            current.next=l1
            l1=l1.next
            
        else:
            
            current.next=l2
            l2=l2.next
            
        current=current.next
        
    
    if l1:
        
        current.next=l1
    
    elif l2:
        
        current.next=l2
        
    return dummy.next

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end=" ")
        curr=curr.next
        
        
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

print("List 1:")
print_list(l1)

print("List 2:")
print_list(l2)

# Merging the two lists
merged_head = merge_linked_list(l1, l2)

print("Merged List:")
print_list(merged_head)
        
        
            