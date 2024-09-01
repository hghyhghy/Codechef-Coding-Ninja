# You are given two sorted linked lists. You have to merge them to produce a combined sorted linked list. You need to return the head of the final linked list.

# Note:

# The given linked lists may or may not be null.
# For example:

# If the first list is: 1 -> 4 -> 5 -> NULL and the second list is: 2 -> 3 -> 5 -> NULL

# The final list would be: 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> NULL

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def merge_list(list1,list2):
    
    dummy=ListNode()
    curr = dummy
    
    p1=list1
    p2=list2
    
    while p1 and p2:
        
        if p1.val < p2.val:
            
            curr.next = p1
            p1=p1.next
            
        else:
            
            curr.next=p2
            p2=p2.next
            
            
        curr=curr.next
        
    
    if p1:
        
        curr.next =p1
        
    if p2:
        
        curr.next=p2
        
    
    return dummy.next

def print_list(head):
    
    curr=head
    
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next


list1 = ListNode(1, ListNode(3, ListNode(5)))

# Create second sorted linked list: 2 -> 4 -> 6
list2 = ListNode(2, ListNode(4, ListNode(6)))

# Merge the lists
merged_list = merge_list(list1, list2)

print_list(merged_list)
    
