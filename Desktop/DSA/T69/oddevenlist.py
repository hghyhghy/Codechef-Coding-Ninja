# Problem statement
# You are given a singly linked list ‘HEAD’ consisting of ‘N’ nodes. The task is to group all the odd nodes together, followed by the even nodes, maintaining the relative order of nodes given in the input. Note that we are talking about the node’s positions and not the value stored in the node. Try to write an in-place algorithm (i.e., without using any extra space) to solve this problem.

# Example:
# Given linked list: ‘2 => 1 => 3 => 4 => 6 => 5’

# While maintaining the relative order of nodes as it is in the input, Nodes at odd positions are (2, 3, 6), and nodes at evens position are (1, 4, 5).

# Modified linked list: ‘2 => 3 => 6 => 1 => 4 => 5’

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def odd_even_position_list(head):
    
    if not head or not head.next:
        
        return head
    
    odd=head
    even=head.next
    even_head=even
    
    while even and even.next:
        
        odd.next=even.next
        odd=  odd.next
        even.next=odd.next
        even=even.next
        
    odd.next = even_head
    
    return head

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

print("Original List:")
print_list(head)

# Reorganizing the list
new_head = odd_even_position_list(head)

print("Reorganized List (Odd-Even positions):")
print_list(new_head)