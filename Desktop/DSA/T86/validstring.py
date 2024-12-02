class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

def oddEvenList(head: Node) -> Node:
    if not head:
        return None
    
    # Pointers for odd and even nodes
    odd_head = odd_current = Node(0)  # Dummy head for odd list
    even_head = even_current = Node(0)  # Dummy head for even list
    
    current = head
    index = 0
    
    # Traverse the list and separate odd and even indexed nodes
    while current:
        if index % 2 == 0:  # Odd index (0-based means 0, 2, 4 are even indices)
            odd_current.next = current
            odd_current = odd_current.next
        else:  # Even index
            even_current.next = current
            even_current = even_current.next
        current = current.next
        index += 1

    # Connect the last node of odd list to the head of even list
    odd_current.next = even_head.next  # Skip the dummy head
    even_current.next = None  # End the even list

    return odd_head.next  # Return the head of the reordered list

def print_linked_list(head: Node):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")  # End of list indication

# Example usage
input_values = [1,3,5,7]
head = Node(input_values[0])
current = head
for value in input_values[1:]:
    current.next = Node(value)
    current = current.next

new_head = oddEvenList(head)
print_linked_list(new_head)  # Output: 1 -> 3 -> 5 -> 2 -> 4 -> None
