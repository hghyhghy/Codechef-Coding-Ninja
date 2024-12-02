

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head,target):

    curr=head
    
    if head == target:
        
        return head.next
    
    while curr.next and curr.next.val != target:
        
        curr=curr.next
        
    if curr.next:
        
        curr.next=curr.next.next
        
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

# Deleting node with value 3
head = main(head, 3)

current = head
while current:
    print(current.val, end=' ')
    current = current.next