# Problem statement
# A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.



# You are given a sorted doubly linked list of size 'n', consisting of distinct positive integers, and a number 'k'.



# Find out all the pairs in the doubly linked list with sum equal to 'k'.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def pair_with_given_sum(head,target):
    
    outer=head
    while outer:
        
        inner=outer.next
        
        while inner:
            
            if inner.val+outer.val == target:
                
                return (inner.val,outer.val)
            
            inner=inner.next
            
        outer=outer.next
        
    return None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

target = 7
result = pair_with_given_sum(head, target)

if result:
    print(f"Pair with sum {target}: {result}")
else:
    print(f"No pair with sum {target} found.")