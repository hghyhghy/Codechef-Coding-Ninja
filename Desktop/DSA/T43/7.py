# delete a target node from the linked list 

class Node:

    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def delete_node(head,target):
    
    dummy=Node(0)
    dummy.next=head
    curr=dummy
    
    while curr.next:
        
        if curr.next.val == target:
            
            curr.next = curr.next.next
            
            break
        
        curr=curr.next
        
    return dummy.next

def print_list(head):
    
    curr=head
    while  curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
        
# Remove N-th node from the end of a Linked List

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def deleting_nth_node(head,k):
    
    dummy=Node(0)
    dummy.next=head
    fast=slow=dummy
    
    for _ in range(k+1):
        
        fast=fast.next
        
    while fast:
        
        fast=fast.next
        slow=slow.next
        
    slow.next = slow.next.next
    
    
    return dummy.next

def print_list(head):
    
    curr=head
    
    while curr:
        
        print(curr.val, end=" ->")
        curr = curr.next
        
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    arr = [1, 2, 3, 4, 5]
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    print("Original Linked List:")
    print_list(head)
    
    # Remove the 2nd node from the end (which is 4 in this case)
    n = 3
    head = deleting_nth_node(head, n)
    
    print("Linked List after removal:")
    print_list(head)
    
    