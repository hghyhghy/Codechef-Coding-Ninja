# Problem statement
# Given a singly linked list of integers. Your task is to return the head of the reversed linked list.

# For example:
# The given linked list is 1 -> 2 -> 3 -> 4-> NULL. Then the reverse linked list is 4 -> 3 -> 2 -> 1 -> NULL and the head of the reversed linked list will be 4.
# Follow Up :
# Can you solve this problem in O(N) time and O(1) space complexity?

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def reverse_main(head):
    
    if not head:
        
        return None
    
    currnt=head
    prev =None
    
    while currnt:
        
        node=currnt.next
        currnt.next=prev
        prev= currnt
        currnt=node
        
    return prev 

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end=" ")
        curr=curr.next
        
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
print_list(head)

reversed_head = reverse_main(head)

print("\nReversed Linked List:")
print_list(reversed_head)

