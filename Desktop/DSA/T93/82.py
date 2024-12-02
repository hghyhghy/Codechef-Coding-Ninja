
#palindrome list 
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
        
        new=stack.pop()
        
        if new != curr.val:
            
            return False
        
        curr=curr.next
        
    return True

print(main())