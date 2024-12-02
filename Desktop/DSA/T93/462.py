#delete the kth node

class Node:

    def __init__(self,val=0,next=None):

        self.val = val
        self.next = next


def main(head,k):

    dummy=Node(0)
    dummy.next=head

    slow=head
    fast=head

    for _ in range(k):

        fast=fast.next


    while fast:

        slow=slow.next
        fast=fast.next

    slow.next=slow.next.next

    return  dummy.next

def print_list(head):

    curr=head
    while curr:

        print(curr.val,end="->")
        curr=curr.next

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
head = main(head, 2)

# Expected output: 1 -> 2 -> 3 -> 5 -> None
print_list(head)
