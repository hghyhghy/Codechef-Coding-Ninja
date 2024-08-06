# Find middle element in a Linked List


# 70

# 3
# Problem Statement: Given the head of a linked list of integers, determine the middle node of the linked list. However, if the linked list has an even number of nodes, return the second middle node.

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def finding_middle(head):
    
    fast=slow=head
    
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        
    return slow

def print_list(head):
    
    curr = head
    while curr:
        
        print(curr.val , end="->")
        curr=curr.next
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    arr = [1, 2, 3, 4, 5]
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    print("Linked List:")
    print_list(head)
    
    # Find the middle node
    middle = finding_middle(head)
    
    print("Middle Node Value:")
    if middle:
        print(middle.val)
    else:
        print("List is empty")