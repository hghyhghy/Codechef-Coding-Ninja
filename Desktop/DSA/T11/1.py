# merge two list 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def merging_linked_list(l1,l2):
    
   
    
    dummy=ListNode()
    current = dummy
    
    while l1 and l2:
        
        if l1.val <= l2.val:
            
            current.next =  l1
            l1=l1.next
            
        else:
            
            current.next=l2
            l2=l2.next
        
        current=current.next
        
    if l1:
        
        current.next=l1
    if l2:
        current.next=l2
        
    return dummy.next
        
def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
        
l1 = ListNode(1, ListNode(3, ListNode(5)))  # Linked list: 1 -> 3 -> 5
l2 = ListNode(2, ListNode(4, ListNode(6)))  # Linked list: 2 -> 4 -> 6

# Merge the two sorted linked lists
merged_list = merging_linked_list(l1, l2)

# Print the merged list
print("Merged list:")
print_list(merged_list)
    