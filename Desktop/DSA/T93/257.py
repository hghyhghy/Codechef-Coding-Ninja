

#merge list 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(p1,p2):  

    dummy=ListNode()
    curr=dummy
    
    while p1 and p2:
        
        if p1.val < p2.val:
            
            curr.next=p1
            p1=p1.next
            
        else:
            
            curr.next=p2
            p2=p2.next
            
        curr=curr.next
        
    
    if p1:
        
        curr.next=p1
        
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
merged_list = main(list1, list2)

print_list(merged_list)
        
        