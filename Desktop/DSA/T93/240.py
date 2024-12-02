

#remove duplicates from linked list 


class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(head):
    
    curr=head
    prev=None
    
    seen=set()

    while curr:
        
        if curr.val in seen:
            
            prev.next=curr.next
            
        else:
            
            seen.add(curr.val)
            prev=curr
            
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
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(1)


print("Original list:")
print_list(head)

# Removing duplicates
head = main(head)

print("List after removing duplicates:")
print_list(head)