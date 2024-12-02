# Problem statement
# You have been given a singly Linked List of 'N' nodes with integer data and an integer 'K'.



# Your task is to remove the 'K'th node from the end of the given Linked List and return the head of the modified linked list.



# Example:
# Input : 1 -> 2 -> 3 -> 4 -> 'NULL'  and  'K' = 2
# Output: 1 -> 2 -> 4 -> 'NULL'
# Explanation:
# After removing the second node from the end, the linked list become 1 -> 2 -> 4 -> 'NULL'.

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def kth_node(head,k):
    
    dummy=Node(0)
    dummy.next=head
    
    fast=head
    slow=head
    
    for _ in range(k):
        
        fast=fast.next
        
        
    while fast:
        
        slow=slow.next
        fast=fast.next
        
    slow.next=slow.next.next
    
    return dummy.next

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Delete the 2nd node from the end (node with value 4)
head = kth_node(head, 2)

# Expected output: 1 -> 2 -> 3 -> 5 -> None
printList(head)