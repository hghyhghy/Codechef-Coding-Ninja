# Detect a Cycle in a Linked List

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def detecting_loop(head):
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
        
        if slow ==  fast:
            
            return True
        
    
    return False

def print_list(head):
    
    curr = head
    
    while curr:
        
        print(curr.val , end=" -> ")
        curr=curr.next
        

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    arr = [1, 2, 3, 4, 5]
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    # Introduce a cycle: 5 -> 2
    current.next = head.next  # Create a cycle by linking last node to second node

    # Check for cycle
    if detecting_loop(head):
        print("The linked list has a cycle.")
    else:
        print("The linked list does not have a cycle.")