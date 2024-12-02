# There is a singly-linked list head and we want to delete a node node in it.

# You are given the node to be deleted node. You will not be given access to the first node of head.

# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def delete_node(node):
    
    if not node:
        
        return None
    
    node.val=node.next.val
    node.next=node.next.next
    
def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end= " ")
        curr=curr.next
        
        
node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4

# Print the original linked list
print("Original Linked List:")
print_list(node1)

# Delete the node with value 5
delete_node(node2)

# Print the modified linked list
print("Linked List after deleting node with value 5:")
print_list(node1)