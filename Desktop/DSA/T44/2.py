# lenght of the linked list 

class ListNode:
    
    def __init__(self,val= 0, next=None):
        
        self.val=val
        self.next=next
        
def count_length_of_the_linkedlist(head):
    
    if not head:
        return None
    
    count  = 0
    current= head
    
    while current:
        
        count += 1
        current=current.next

    if count % 2 == 0:
        
        return "Even lenght"
    else:
        
        return "Odd lenght"

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))



length = count_length_of_the_linkedlist(head)
print(f"Length of the linked list: {length}")

        
        