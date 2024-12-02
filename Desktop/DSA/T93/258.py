
#smallest element in the linked list 

class Node:
    
    def  __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head):
    
    smallest=head.val
    curr=head.next
    
    while curr:
        
        if curr.val < smallest:
            
            smallest = curr.val
            
        curr=curr.next
        
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

print(main(node1))