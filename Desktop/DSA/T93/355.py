

class ListNode:

    def __init__(self,val=0,next=None):

        self.val=val
        self.next=next


def main(head):

    current=head
    prev=None

    visited=set()

    while current:

        if current.val in visited:

            prev.next=current.next

        else:

            visited.add(current.val)
            prev=current

        current=current.next


    return  head

def print_list(head):

    curr=head
    while curr:

        print(curr.val,end="->")
        curr=curr.next


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(3)

head=main(head)

print_list(head)
