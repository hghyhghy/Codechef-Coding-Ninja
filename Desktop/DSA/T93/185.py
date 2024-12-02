

#split two  linked list 
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
        
    second=slow.next
    slow.next=None
    
    return head,second

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    nodes = [1, 2, 3, 4, 5]
    head = ListNode(nodes[0])
    current = head
    for value in nodes[1:]:
        current.next = ListNode(value)
        current = current.next

    print("Original Linked List:")
    print_list(head)
    
    # Split the linked list
    first_half, second_half = main(head)
    
    print("First Half:")
    print_list(first_half)
    
    print("Second Half:")
    print_list(second_half)