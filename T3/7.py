# Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        
        self.next=next
        
        
def deleting_duplicate(head):
    
    if not head:
        
        return None
    
    seen=set()
    curr = head
    prev = None
    
    while curr:
        
        if curr.val in seen:
            
            prev.next  = curr.next
            
        else:
            
            seen.add(curr.val)
            prev = curr
            
            
        curr =curr.next
        
        
    return head


def print_list(head):
    
    curr =  head
    
    while curr:
        
        print(curr.val , end=" ")
        curr =curr.next
        
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(4, ListNode(1))))))

print("Original List:")
print_list(head)

head = deleting_duplicate(head)

print("List after removing duplicates:")
print_list(head)
        
