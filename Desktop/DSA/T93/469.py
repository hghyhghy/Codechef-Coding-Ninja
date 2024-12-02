
#delete alternative

class Node:

    def __init__(self,val=0,next=None):

        self.val = val
        self.next = next


def main(head):

    curr=head

    while curr and curr.next:

        new= curr.next
        curr.next=new.next
        curr=curr.next

def print_list(head):

    curr=head
    while curr:

        print(curr.val,end="->")
        curr=curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

print("Original List:")
print_list(head)

# Deleting alternate nodes
main(head)

print("\nList after deleting alternate nodes:")
print_list(head)