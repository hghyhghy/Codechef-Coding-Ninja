# Reverse a Linked List

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def reverse_linked_list(head):
    
    current= head 
    prev=None
    
    while current:
        
        next_node = current.next
        current.next=prev
        prev=current
        current=next_node
        
    return prev

def print_list(head):
    
    current = head
    
    while current:
        
        print(current.val,end="->")
        current=current.next
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    arr = [1, 2, 3, 4, 5]
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    print("Original Linked List:")
    print_list(head)
    
    # Call the reverse_linked_list function and print the result
    reversed_head = reverse_linked_list(head)
    print("Reversed Linked List:")
    print_list(reversed_head)