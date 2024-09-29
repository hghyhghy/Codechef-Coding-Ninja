# Problem statement
# You have been given a singly Linked List of integers. Your task is to divide this list into two smaller singly-linked lists in which the nodes appear in alternating fashion from the original list.

# For example:
# If the given linked list is 1 -> 2 -> 3 -> 4 -> 5 -> NULL

# The first sub-list is 1 -> 3 -> 5 -> NULL.
# The second sub-list is 2 -> 4 -> NULL.
# If it is impossible to make any of the two smaller sub-lists, return an empty list i.e. NULL.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def splitting_list(head):
    
    if not head:
        
        return None
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
    second_half= slow.next
    slow.next=None
    
    return head,second_half

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
    first_half, second_half = splitting_list(head)
    
    print("First Half:")
    print_list(first_half)
    
    print("Second Half:")
    print_list(second_half)