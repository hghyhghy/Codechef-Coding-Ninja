# Problem statement
# Given a singly linked list of 'N' nodes. Your task is to delete the middle node of this list and return the head of the modified list.



# However, if the list has an even number of nodes, we delete the second middle node



# Example:
# If given linked list is 1->2->3->4 then it should be modified to 1->2->4.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def delete_middle_node(head):

    if not head:
        
        return None
    
    prev=None
    slow=head
    fast=head
    
    while fast and fast.next:
        
        prev=slow
        slow=slow.next
        fast=fast.next.next
        
        
    if prev:
        
        prev.next=slow.next
        
        
    return head

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
print_list(head)

# Deleting the middle node
head = delete_middle_node(head)

print("After Deleting Middle Node:")
print_list(head)
    