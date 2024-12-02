# reverse the linked list

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main_reverse(head):
    
    if not head:
        
        return
    
    current=head
    prev=None
    
    while current:
        
        new_node=current.next
        current.next=prev
        prev=current
        current=new_node
        
    return prev

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end=" ->")
        curr=curr.next
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original List:")
print_list(head)

# Reverse the list
reversed_head = main_reverse(head)

print("Reversed List:")
print_list(reversed_head)