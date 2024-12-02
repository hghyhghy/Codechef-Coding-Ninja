# Insert a Node in a Linked List

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def insert_at_the_end(head,value):
    
    new_node=Node(value)

    if head is None:
        
        return value
    
    current = head
    while current.next:
        
        current=current.next
        
    current.next = new_node
    
    return head

def print_list(head):
    
    curr = head
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
head = Node(1, Node(2, Node(3)))

print("Original list:")
print_list(head)

head = insert_at_the_end(head, 4)
print("After inserting at the end:")
print_list(head)