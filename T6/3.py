# Delete the Middle Node of the Linked List


class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def deleting_middle_node(head):
    
    if not head or not head.next:
        
        return None
    
    fast=slow=head
    prev=None
    
    while fast and fast.next:
        
        fast=fast.next.next
        prev=slow
        slow=slow.next
        
    if prev:
        
        prev.next=slow.next 
        
        
    return head

def print_list(head):
    
    curr = head
    while curr:
        
        print(curr.val,end=" -> ")
        curr=curr.next
        
        
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
    
    # Delete the middle node
    head = deleting_middle_node(head)
    
    print("Linked List after deleting the middle node:")
    print_list(head)