
#merge list

class Node:

    def __init__(self,val=0,next=None):

        self.val = val
        self.next = next


def main(l1,l2):

    dummy=Node(0)
    curr=dummy

    p1=l1
    p2=l2

    while p1 and p2:

        if p1.val < p2.val:

            curr.next=p1
            p1=p1.next

        else:

            curr.next=p2
            p2=p2.next


        curr=curr.next


    return  dummy.next


def printList(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next


head1 = Node(1)
head1.next = Node(4)
head1.next.next = Node(5)

# Creating the second linked list: 2 -> 3 -> 5 -> NULL
head2 = Node(2)
head2.next = Node(3)
head2.next.next = Node(5)

print("First List:")
printList(head1)

print("Second List:")
printList(head2)

# Merging the two lists
merged_head = main(head1, head2)

print("Merged List:")
printList(merged_head)
