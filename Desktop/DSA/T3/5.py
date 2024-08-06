# delete the nth node from the linked list 

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        

def delete_nth_node(head,n):
    
    dummy=ListNode(0)

    dummy.next =  head
    
    fast= dummy
    slow=dummy
    
    
    for _ in range(n+1):
        
        if not fast:
            
            return head
        
        fast=fast.next
        
    while fast is not None:
        
        fast=fast.next
        slow=slow.next
        
    slow.next=slow.next.next
    
    
    return dummy.next

def print_list(head):
    
    curr=head
    
    while curr:
        
        print(curr.val, end=" ")

        curr=curr.next
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original list:")
    print_list(head)

    # Delete the 2nd node (index 2): list should become 1 -> 2 -> 4 -> 5
    new_head = delete_nth_node(head, 3)
    
    print("List after deleting 2nd node:")
    print_list(new_head)