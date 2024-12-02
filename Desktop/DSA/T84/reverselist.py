# Problem statement
# You have been given a singly linked list of integers. Write a function to print the list in a reverse order.

# To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.

# Note :
# You can’t change any of the pointers in the linked list, just print the linked list in the reverse order.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def reverse_list(head):
    
    if not head:
        
        return 
    
    reverse_list(head.next)

    print(head.val, end=" ")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Function call to print the list in reverse
reverse_list(head)

