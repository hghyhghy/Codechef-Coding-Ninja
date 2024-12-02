

#intersection 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def main(h1,h2):
    
    if not h1 or not h2:
        
        return None
    
    p1=h1
    p2=h2
    
    while p1 != p2:
        
        p1=p1.next if p1 else h2
        p2=p2.next if p2 else h1
        
    return p1

c1 = ListNode(8, ListNode(4, ListNode(5)))
a1 = ListNode(4, ListNode(1, c1))
b1 = ListNode(5, ListNode(0, ListNode(1, c1)))

print(main(a1,b1).val)