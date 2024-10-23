# Problem statement
# You are given two Singly Linked Lists of integers, which may have an intersection point.

# Your task is to return the first intersection node. If there is no intersection, return NULL.



# Example:-
# The Linked Lists, where a1, a2, c1, c2, c3 is the first linked list and b1, b2, b3, c1, c2, c3 is the second linked list, merging at node c1.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def intersection(l1,l2):
    
    if not l1 or not l2:
        
        return None
    
    p1=l1
    p2=l2
    
    while p1 != p2:
        
        p1=p1.next if p1 else l2
        p2=p2.next if p2 else l1
        
    return p1

intersecting_node = ListNode(6, ListNode(7))

# Creating first list
l1 = ListNode(1, ListNode(2, ListNode(3, intersecting_node)))

# Creating second list
l2 = ListNode(4, ListNode(5, intersecting_node))

# Finding intersection
intersection = intersection(l1, l2)

# Print the intersection node value
if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")