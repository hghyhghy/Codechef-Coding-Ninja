
class ListNode:
    
    def  __init__(Self,val=0,next=None):
        
        Self.val=val
        Self.next=next
        
def main(head):

    curr=head
    prev=None
    
    while curr:
        
        node=curr.next
        curr.next=prev
        prev=curr
        curr=node
        
    head=prev
    return head

def print_list(head):
    
    curr=head
    
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reversed_head = main(head)
print_list(reversed_head)