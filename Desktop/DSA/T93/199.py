
#delete the middle node
class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def main(head):
    
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
        
        print(curr.val,end="->")
        curr=curr.next
        

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
print_list(head)

# Deleting the middle node
head = main(head)

print("After Deleting Middle Node:")
print_list(head)
    