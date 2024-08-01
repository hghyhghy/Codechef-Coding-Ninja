# finding the lenght of the linked list odd or even 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def detecting_length_of_list(head):
    
    if not head:
        
        return None
    
    count = 0 
    current = head
     
    while current :
        
        count += 1
        
        current = current.next
        
        
    if count % 2 == 0:
        
        return "Even length"

    elif count % 2 !=0:
        
        return "Odd lenght "


def print_list(head):
    
    curr =  head
    
    while curr:
        
        print(curr.val , end = " ")
        curr =curr.next
        
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original list:")
    print_list(head)

    # Check if the length of the linked list is odd or even
    result = detecting_length_of_list(head)
    print(f"Length of the linked list is: {result}")