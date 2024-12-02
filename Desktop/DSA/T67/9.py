# Problem statement
# You are given a singly linked list that may or may not contain a cycle. You are supposed to return the node where the cycle begins, if a cycle exists, else return 'NULL'.



# A cycle occurs when a node's next pointer returns to a previous node in the list.



# Example:
# In the given linked list, there is a cycle starting at position 0, hence we return 0

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def cycle_node(head):
    
    visited=set()
    current=head
    
    while current:
        
        if current in visited:
            
            return current.val
        
        visited.add(current)
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
node5.next = node3  # Creates a cycle

# Detect the cycle
print(cycle_node(head))

