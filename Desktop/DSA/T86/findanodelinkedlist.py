# Problem statement
# You have been given a singly linked list of integers. Write a function that returns the index/position of integer data denoted by 'N' (if it exists). Return -1 otherwise.

# Note :
# Assume that the Indexing for the singly linked list always starts from 0.

class ListNode:
    
    def  __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def find_index_of_element(head,target):
    
    index=0 
    curr=head
    
    
    while curr:
        
        if curr.val == target:
            
            return index
        
        curr =curr.next
        index += 1
        
    
    return -1

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Example usage
head = ListNode(3)
head.next = ListNode(7)
head.next.next = ListNode(10)
head.next.next.next = ListNode(15)

print("Original List:")
print_list(head)

N = 10  # Let's find this value in the list
result = find_index_of_element(head, N)
print(f"Index of {N}: {result}")  # Output: 2 (since 10 is at index 2)