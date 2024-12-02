from numpy.lib.polynomial import roots


#missing number

class ListNode:

    def __init__(self,val=0,next=None):

        self.val=val
        self.next=next


def main(root):

    if not root:

        return

    main(root.next)

    print(root.val,end=" ")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Function call to print the list in reverse
main(head)