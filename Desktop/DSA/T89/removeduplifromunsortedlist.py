# You are given a linked list of N nodes. Your task is to remove the duplicate nodes from the linked list such that every element in the linked list occurs only once i.e. in case an element occurs more than once, only keep its first occurrence in the list.

# For example :
# Assuming the linked list is 3 -> 2 -> 3 -> 4 -> 2 -> 3 -> NULL.

# Number ‘2’ and ‘3’ occurs more than once. Hence we remove the duplicates and keep only their first occurrence. So, our list becomes : 3 -> 2 -> 4 -> NULL.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def remove_dupli_from_unsorted_list(head):
    
    if not head:
        
        return None
    
    current = head
    prev=None
    
    visited=set()

    while current:
        
        if current.val in  visited:
            
            prev.next = current.next
            
        else:
            
            visited.add(current.val)
            prev=current
        
        current=current.next
        
        
    return head

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(3)

head=remove_dupli_from_unsorted_list(head)

print_list(head)
