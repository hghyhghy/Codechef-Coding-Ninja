
#class listnode

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(l1,l2):
    
    dummy=ListNode()
    curr=dummy
    
    while l1 and l2:
        
        if l1.val <= l2.val:
            
            curr.next=l1
            l1=l1.next
            
        else:
            
            curr.next =l2
            l2=l2.next
            
        curr=curr.next

    if l1:
        
        l1=l1.next
        
    if l2:
        
        l2=l2.next
        
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
merged_head = main(l1, l2)

print("Merged List:")
print_list(merged_head)
    
    