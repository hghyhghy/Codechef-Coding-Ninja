#cycle  node

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head):
    
    if not head:
        
        return  None
    
    current = head
    seen=set()
    
    while current:
        
        if current in seen:
            
            return current
        
        seen.add(current)
        current=current.next
        
    return "NULL"

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Link nodes
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

print(main(head))