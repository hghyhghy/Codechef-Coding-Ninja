

#insert at the end 

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main(head,root):
    
    new =Node(root)
    curr=head
    
    while curr.next:
        
        curr=curr.next
        
    curr.next=new 
    
    return head

def print_list(head):
    
    curr = head
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
head = Node(1, Node(2, Node(3)))

print("Original list:")
print_list(head)

head = main(head, 4)
print("After inserting at the end:")
print_list(head)