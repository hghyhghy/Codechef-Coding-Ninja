# Segregate even and odd nodes in LinkedList

class Node:
    
    def __init__(self,val = 0 , next=None):
        
        self.val=val
        self.next=next
        

def separate_odd_even_nodes(head):
    
    if not head:
        
        return None
    
    current = head
    even_dummy  =  Node(0)
    odd_dummy =   Node(0)
    even_node = even_dummy
    odd_node =odd_dummy

    while  current:
        
        if current.val % 2  == 0:
            
            even_node.next =  Node(current.val)
            even_node=even_node.next
            
        else:
            
            odd_node.next=Node(current.val)
            odd_node=odd_node.next
            
        
        current=current.next
        
        
    even_node.next=odd_dummy.next
    
    return even_dummy.next

def print_list(head):
    
    current=  head
    while current:
        
        print(current.val , end="->")
        current=current.next
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 6
    arr = [1, 4, 3, 2, 5, 6]
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    print("Original Linked List:")
    print_list(head)
    
    # Call the segregate_even_odd function and print the result
    segregated_head = separate_odd_even_nodes(head)
    print("Linked List after Segregation:")
    print_list(segregated_head)
