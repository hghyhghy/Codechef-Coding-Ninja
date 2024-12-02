# You have been given a singly Linked List of 'N' nodes with integer data and an integer 'K'.



# Your task is to remove the 'K'th node from the end of the given Linked List and return the head of the modified linked list.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def delete_the_kth_node_from_the_linkedlist(head,k):
    
    dummy=ListNode(0)
    dummy.next=head
    fast=dummy
    slow=dummy
    
    for _ in range(k):
        
        fast =fast.next
        
    while fast.next:
        
        fast=fast.next
        slow=slow.next
        
    slow.next=slow.next.next
    
    return dummy.next

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end="->")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
print_list(head)

# Remove the 2nd node from the end
head = delete_the_kth_node_from_the_linkedlist(head, 2)

print("List after removing 2nd node from the end:")
print_list(head)