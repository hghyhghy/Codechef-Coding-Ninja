class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findIntersection(l1, l2):  # Renamed the function to avoid conflict
    stack1 = []
    stack2 = []

    # Traverse first list and push its values to stack1
    curr = l1
    while curr:
        stack1.append(curr)
        curr = curr.next

    # Traverse second list and push its values to stack2
    curr1 = l2
    while curr1:
        stack2.append(curr1)
        curr1 = curr1.next

    # Find the intersection point
    intersection = None
    while stack1 and stack2:
        node1 = stack1.pop()
        node2 = stack2.pop()

        if node1 == node2:
            intersection = node1
        else:
            break

    return intersection

# Create the intersection part of the list
common_part = ListNode(5, ListNode(7, ListNode(9)))

# Create the lists
listA = ListNode(1, ListNode(3, common_part))
listB = ListNode(2, ListNode(4, ListNode(6, common_part)))

# Find intersection
intersection_node = findIntersection(listA, listB)  # Use the renamed function
if intersection_node:
    print(f"Intersection at node with value: {intersection_node.val}")
else:
    print("No intersection")
