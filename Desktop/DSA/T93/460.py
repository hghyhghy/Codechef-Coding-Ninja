
class ListNode:

    def  __init__(self,val=0,next=None):

        self.val=val
        self.next=next


def  delete(node):

    node.val=node.next.val
    node.next=node.next.next


def print_list(head):

    curr=head

    while curr:

        print(curr.val,end="->")
        curr=curr.next


head = ListNode(4)
node1 = ListNode(5)
node2 = ListNode(1)
node3 = ListNode(9)
head.next = node1
node1.next = node2
node2.next = node3

# Delete node with value 5
delete(node1)

print_list(head)




