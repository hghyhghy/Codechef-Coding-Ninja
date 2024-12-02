# Problem statement
# You are given a linked list of N nodes. Your task is to remove the duplicate nodes from the linked list such that every element in the linked list occurs only once i.e. in case an element occurs more than once, only keep its first occurrence in the list.

# For example :
# Assuming the linked list is 3 -> 2 -> 3 -> 4 -> 2 -> 3 -> NULL.

# Number ‘2’ and ‘3’ occurs more than once. Hence we remove the duplicates and keep only their first occurrence. So, our list becomes : 3 -> 2 -> 4 -> NULL.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def removing_the_duplicate_from_the_list(head):
    
    current=head
    prev=None
    
    seen=set()

    if not head:
        
        return None
    
    while current:
        
        if current.val in seen:
            
            prev.next=current.next
            
        else:
            
            seen.add(current.val)
            prev=current
            
        current=current.next
        
    
    return head

def print_list(head):
    
    current=head
    
    while current:
        
        print(current.val, end="->")
        current=current.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(1)


print("Original list:")
print_list(head)

# Removing duplicates
head = removing_the_duplicate_from_the_list(head)

print("List after removing duplicates:")
print_list(head)