# Find The Lowest Value in a Linked List

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def lowest_value(head):
    
    smallest=head.val
    current=head.next
    
    while current:
        
        if current.val < smallest:
            
            smallest = current.val
            
        current =current.next
        
    return smallest

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(lowest_value(node1))