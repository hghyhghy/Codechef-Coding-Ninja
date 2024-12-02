
#linked list  deletion from  position

class ListNode:

    def __init__(self,val=0,next=None):

        self.val=val
        self.next=next



def main(head,pos):

    if not head:

        return  0

    if pos == 0:

        return  head.next


    current=head

    for _ in range(pos-1):

        if current and current.next:

            current=current.next

        else:

            return  head

    if current.next is not None:

        current.next=current.next.next

    return  head


def print_list(head):

    curr=head
    while curr:

        print(curr.val,end="->")
        curr=curr.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original linked list:")
print_list(head)

# Delete node at position 2 (value 3)
head = main(head, 2)

print("Linked list after deletion:")
print_list(head)

