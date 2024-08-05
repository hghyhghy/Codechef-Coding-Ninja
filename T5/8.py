# Check if the given Linked List is Palindrome using stack 

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def palindrome_linked_list(head):
    
    if not head or not head.next:
        
        return True
    
    stack=[]
    current = head 
    
    while current:
        
        stack.append(current.val)
        current=current.next
        
        
    current = head 
    
    while current:
        
        if current.val != stack.pop():
            
            return False
        
        current=current.next
        
    return True

def print_list(head):
    
    curr =  head
    while curr:
        
        print(curr.next, end=" -> ")
        curr = curr.next 
        
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
    arr = [1, 2, 3, 2, 3]
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    print("Linked List:")
    print_list(head)
    
    # Call the is_palindrome function and print the result
    if palindrome_linked_list(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")
    
