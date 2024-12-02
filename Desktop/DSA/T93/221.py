
class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(head,target):

    if head == target:
        
        return True
    
    curr=head
    
    while curr:
        
        if curr.val == target:
            
            return True
        
        curr=curr.next
        
    return False

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(main(head,3))
