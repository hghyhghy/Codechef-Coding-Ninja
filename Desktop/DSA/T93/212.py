
#pair wih given sum

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head,target):
    
    outer=head
    while outer:
        
        inner=outer.next
        
        while inner:
            
            if(inner.val+outer.val) == target:
                
                return(inner.val,outer.val)

            inner=inner.next
            
        outer=outer.next
        
    return None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

target = 7
result = main(head, target)

if result:
    print(f"Pair with sum {target}: {result}")
else:
    print(f"No pair with sum {target} found.")