

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head):
    
    curr=head
    
    stack=[]
    while curr:
        
        stack.append(curr.val)
        curr=curr.next
        
    curr=head
    
    while curr:
        
        if curr.val != stack.pop():
            
            return False
        
        curr=curr.next
        
    return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(main(head))