# You are given a singly linked list ‘HEAD’ consisting of ‘N’ nodes. The task is to group all the odd nodes together, followed by the even nodes, maintaining the relative order of nodes given in the input. Note that we are talking about the node’s positions and not the value stored in the node. Try to write an in-place algorithm (i.e., without using any extra space) to solve this problem.

class ListNode:
    
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
def odd_even_indexed_elements(head):
    
    if not head:
        
        return
    
    odd=head
    even=head.next
    even_head=even
    
    while even and even.next:
        
        odd.next = even.next
        odd=odd.next
        
        even.next=odd.next
        even=even.next
        
    odd.next=even_head
    
    return head

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val ,end=" ")
        curr=curr.next
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Rearrange linked list to odd-even: 1 -> 3 -> 5 -> 2 -> 4
new_head = odd_even_indexed_elements(head)
print_list(new_head) 
