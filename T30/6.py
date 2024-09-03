class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_function(head):
    curr = head
    prev = None
    while curr:
        node = curr.next
        curr.next = prev
        prev = curr
        curr = node
    return prev

def add_two_number(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    list1 = reverse_function(list1)
    list2 = reverse_function(list2)

    carry = 0
    current = dummy

    while list1 or list2 or carry:
        v1 = list1.val if list1 else 0
        v2 = list2.val if list2 else 0

        total = v1 + v2 + carry
        carry = total // 10

        current.next = ListNode(total % 10)
        current = current.next

        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next

    store=reverse_function(dummy.next)

    return store


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()  # for new line

# Example usage
l1 = ListNode(2, ListNode(4, ListNode(3)))  # represents number 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # represents number 465

result = add_two_number(l1, l2)
print_list(result)  # Output should represent the number 807 (7 -> 0 -> 8)
