
#count even and odd length linked list 
class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head):
    
    curr=head
    count= 0
    while curr:
        
        count += 1
        curr=curr.next
        
    
    if count % 2==0:
        
        return "Even length"

    else:
        
        return "Odd length"

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))



length = main(head)
print(f"Length of the linked list: {length}")