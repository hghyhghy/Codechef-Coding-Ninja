
#kth node from the list

class  ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head,k):
    
    if not head:
        
        return None
    
    fast=head
    slow=head
    
    for _ in range(k):
        
        fast=fast.next
        
    
    while fast:
        
        fast=fast.next
        slow=slow.next
        
    
    return slow

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

k = 2
result_node = main(head, k)
if result_node:
    print(f"The {k}-th node from the end is {result_node.val}")
else:
    print(f"There is no {k}-th node from the end in the list")