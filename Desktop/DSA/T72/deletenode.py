# Problem statement
# You are given a Singly Linked List of integers and a reference to the node to be deleted. Every node of the Linked List has a unique value written on it. Your task is to delete that node from the linked list.

# A singly linked list is a linear data structure in which we can traverse only in one direction i.e. from Head to Tail. It consists of several nodes where each node contains some data and a reference to the next node.

# Note:

# • The reference to the head of the linked list is not given.
# • The node to be deleted is not a tail node.
# • The value of each node in the Linked List is unique.
# • It is guaranteed that the node to be deleted is present in the linked list.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next

def delete(node):
    
    node.val=node.next.val
    node.next=node.next.next
    
def printList(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        

head = ListNode(4)
node1 = ListNode(5)
node2 = ListNode(1)
node3 = ListNode(9)
head.next = node1
node1.next = node2
node2.next = node3

# Delete node with value 5
delete(node1)

printList(head)