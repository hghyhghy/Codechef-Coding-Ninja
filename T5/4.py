# find the element in the linked list 

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def finding_element(head,target):
    
    current =  head
    
    while current:
        
        if current.val ==  target:
            
            return 1
        
        current=current.next

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3
    arr = [1, 2, 3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])

    val = 3  # Element to be checked for presence in the linked list

    # Call the check_if_present function and print the result
    print(finding_element(head, val))

        
        
        