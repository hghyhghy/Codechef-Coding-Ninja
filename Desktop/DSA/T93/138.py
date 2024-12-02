

#delete node

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(head,target):
    
    if not head or not target:
        
        return None
    
    if head.val == target:
        
        return head.next
    
    curr=head
    
    while curr.next:
        
        if curr.next.val == target:
            
            curr.next=curr.next.next
            
        curr=curr.next
        
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

print("Original list:")
print_list(head)

# Delete node with value 3
head = main(head, 3)

print("List after deleting node with value 3:")
print_list(head)
            
            