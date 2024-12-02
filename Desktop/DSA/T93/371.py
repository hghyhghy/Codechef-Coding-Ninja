

#find a node in the linked list

class ListNode:

    def __init__(self,val=0,next=None):

        self.val=val
        self.next=next


def main(head,target):

    curr=head
    index=0

    while curr:

        if curr.val ==  target:

            return  index

        curr=curr.next
        index +=1

    return  -1

def print_list(head):

    curr=head
    while curr:

        print(curr.val,end="->")
        curr=curr.next


head = ListNode(3)
head.next = ListNode(7)
head.next.next = ListNode(10)
head.next.next.next = ListNode(15)

print("Original List:")
print_list(head)

N = 10  # Let's find this value in the list
result = main(head, N)
print(f"Index of {N}: {result}")