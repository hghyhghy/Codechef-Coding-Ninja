
#delet node from given position 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head,pos):
    
    if not head or not  pos:
        
        return -1
    
    curr =head
    for _ in range(pos-1):
        
        if curr and curr.next:
            
            curr = curr.next
            
        else:
            
            return head
        
    
    if curr.next is not None:
        
        curr.next=curr.next.next
        
    return head

def print_list(head):
    
    curr=head
    while  curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original linked list:")
print_list(head)

# Delete node at position 2 (value 3)
head = main(head, 2)

print("Linked list after deletion:")
print_list(head)