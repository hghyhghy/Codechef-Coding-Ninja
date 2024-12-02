# Given a singly linked list of integers. Your task is to return the head of the reversed linked list.

class ListNode:
    
    def  __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def list_reversal(head):
    
    if not head:
        
        return None
    
    prev=None
    current=head
    
    while current:
        
        node=current.next
        current.next=prev
        prev=current
        current=node
        
    
    return  prev


def print_list(head):
    
    current = head
    
    while current:
        
        print(current.val, end=" ")
        current =current.next
        

if __name__ == "__main__":
    # Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original List:")
    print_list(head)
    
    reversed_head = list_reversal(head)
    
    print("Reversed List:")
    print_list(reversed_head)

