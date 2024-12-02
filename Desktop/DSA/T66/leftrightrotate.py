# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def reverse_list(head,left,right):
    
    dummy=ListNode(0)
    dummy.next = head
    prev= dummy
    
    for _ in range(left-1):
        
        prev =prev.next
        
    ptr1 =  prev.next
    current = ptr1.next
    
    for _ in range(right-left):
        
        ptr1.next= current.next
        current.next=prev.next
        prev.next=current
        current=ptr1.next
        
    return dummy.next

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

    # Initialize the solution and call reverseBetween
left = 2
right = 4
new_head = reverse_list(head, left, right)

print("List after reversing between positions", left, "and", right, ":")
print_list(new_head)
        