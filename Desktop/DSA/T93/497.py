

# cycle detection

class Node:

    def __init__(self,val,next=None):

        self.val=val
        self.next=next


def main(head):

    seen=set()
    current=head

    while  current:

        if current in  seen:

            return  current.val

        seen.add(current)
        current=current.next

    return  -1


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Link nodes
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Creates a cycle

# Detect the cycle
print(main(head))