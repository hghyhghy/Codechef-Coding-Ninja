# You have been given two singly Linked Lists, where each of them represents a positive number without any leading zeros.

# Your task is to add these two numbers and print the summation in the form of a linked list.

# Example:
# If the first linked list is 1 -> 2 -> 3 -> 4 -> 5 -> NULL and the second linked list is 4 -> 5 -> NULL.

# The two numbers represented by these two lists are 12345 and 45, respectively. So, adding these two numbers gives 12390. 

# So, the linked list representation of this number is 1 -> 2 -> 3 -> 9 -> 0 -> NULL

class Node:
    
    def  __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def add_list(first,second):
    
    dummy = Node(0)
    curr = dummy
    carry = 0
    
    while first and second:
        
        d1=first.val if first else 0
        d2=second.val if second else 0
        
        total =  d1+d2+carry
        carry=  total //10
        remiander =  total % 10
        
        curr.next=Node(remiander)
        curr=curr.next
        
        if first:
            first=first.next
            
        if second:
            second=second.next
            
    return dummy.next

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val ,end="->")
        curr=curr.next
        
first = Node(3)
first.next = Node(4)
first.next.next = Node(2)

second = Node(4)
second.next = Node(6)
second.next.next = Node(5)

# Add the two lists
result = add_list(first, second)

# Print the result list
print("Resultant List: ")
print_list(result) 