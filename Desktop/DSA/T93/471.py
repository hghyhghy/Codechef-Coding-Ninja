from logging import fatal


#kth element from the list

class ListNode:

    def __init__(self,val=0,next=None):

        self.val = val
        self.next = next



def main(head,k):

    slow=head
    fast=head

    for _ in range(k):

        fast=fast.next


    while fast:

        slow=slow.next
        fast=fast.next


    return  slow.val if slow else None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
result = main(head, k)
print(result)


