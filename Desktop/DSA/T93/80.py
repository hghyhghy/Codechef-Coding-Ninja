
#delete middle from the middle 

class Node:

    def __init__(self,val=0,next=None):
        
        
        self.val=val
        self.next=next
        
def main(head):
    
    if not head:
        
        return None
    
    prev=None
    slow=head
    fast=head
    
    while fast and  fast.next:
        
        prev=slow
        slow=slow.next
        fast=fast.next.next
        
        if prev:
            
            prev.next=slow.next
            
    return head

def print_list(head):
    
    curr=head
    while  curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original list:")
print_list(head)

# Delete the middle node
head = main(head)

print("Modified list after deleting middle node:")
print_list(head)


        