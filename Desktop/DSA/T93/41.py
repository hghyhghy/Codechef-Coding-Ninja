#sort linked list 
class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def sort_list(head):
    
    stack=[]
    curr=head
    
    while curr:
        
        stack.append(curr.val)
        curr=curr.next
        
    stack.sort()

    new_stack =  ListNode(stack[0]) if stack else  0 
    curr=new_stack
    
    for val in (stack[1:]):
        
        curr.next =  ListNode(val)
        curr=curr.next
        
    return new_stack

def print_list(head):
    
    cur=head
    while cur:
        
        print(cur.val,end= "->")
        cur=cur.next
        
head = ListNode(1)
head.next = ListNode(-2)
head.next.next = ListNode(3)

print("Original List:")
print_list(head)

sorted_head = sort_list(head)

print("Sorted List by actual value:")
print_list(sorted_head)
    