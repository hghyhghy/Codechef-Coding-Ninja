# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def main_add_function(l1,l2):
    
    def reverse_main(head):
        
        curr=head
        prev=None
        
        while curr:
            
            node=curr.next
            curr.next=prev
            prev=curr
            curr=node
            
        return prev
    
    l1=reverse_main(l1)
    l2=reverse_main(l2)

    carry=0
    dummy=ListNode(0)
    curr=dummy
    
    while l1  or l2 or carry:
        
        v1=l1.val if l1 else 0
        v2=l2.val if l2 else 0
        
        total=v1+v2+carry
        carry = total//10
        remainder=total%10
        
        curr.next=ListNode(remainder)
        curr=curr.next
        
        if l1:
            l1=l1.next
            
        if l2:
            l2=l2.next
            
            
    return reverse_main(dummy.next)   

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val,end="->")
        curr=curr.next
        
# Example usage:
l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))  # 7243
l2 = ListNode(5, ListNode(6, ListNode(4))) 

result=main_add_function(l1,l2)

print_list(result)