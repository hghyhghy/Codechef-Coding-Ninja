# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:


# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
class Solution:
          
    def intersection(self,heada,headb):
        
        if not heada or not headb:
            
            return
        
        p1=heada
        p2=headb
        
        
        while p1 != p2:
            
            p1=p1.next if p1 else headb
            # # Move to the next node in list A, or start list B if reached the end of list A

            p2=p2.next if p2 else heada
            
        return p1


c1 = ListNode(8, ListNode(4, ListNode(5)))
a1 = ListNode(4, ListNode(1, c1))
b1 = ListNode(5, ListNode(0, ListNode(1, c1)))

sol = Solution()
print(sol.intersection(a1, b1).val)
