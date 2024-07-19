
# reverse the linked list 

class ListNode:

    def __init__(self,val=0,next=None):

        self.val=val
        self.next=next


def reverse_list(head):

    if not head:

        return None
    
    prev=None

    current = head 

    while current:

        next_node = current.next
        current.next=prev
        prev=current
        current=next_node

    
    return prev

def print_list(head):

    curr=head
    while curr:

        print(curr.val , end=" ")
        curr=curr.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original list:")
print_list(head)


result = reverse_list(head)
print("Reversed list")
print_list(result)

      


