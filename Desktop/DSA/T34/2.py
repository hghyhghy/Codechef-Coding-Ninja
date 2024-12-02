# Problem statement
# You are given a Singly Linked List of integers and a reference to the node to be deleted. Every node of the Linked List has a unique value written on it. Your task is to delete that node from the linked list.

# A singly linked list is a linear data structure in which we can traverse only in one direction i.e. from Head to Tail. It consists of several nodes where each node contains some data and a reference to the next node.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def delete_node_in_linked_list(head,deleted):
    
    if not head:
        
        return None
    
    if head.val == deleted:
        
        return head.next
    
    current = head
    prev=None
    
    while current and current.val !=  deleted:
        
        prev = current
        current =current.next
        
    if current:
        
        prev.next =  current.next
        
        
    return head

def print_list(head):
    
    current=  head
    while current:
        
        print(current.val, end="->")
        current=current.next
        
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
print_list(head)

# Delete node with value 3
head = delete_node_in_linked_list(head, 3)

print("List after deleting node with value 3:")
print_list(head)