

#middle of the linked list

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head):
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
    return slow

def print_middle(middle_node):
    if middle_node:
        print(f"Middle Node Value: {middle_node.val}")
    else:
        print("The list is empty")
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

middle = main(head)
print_middle(middle)
        