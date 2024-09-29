# kth node from the end of the linst

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
def kth_element_from_last(head,k):
    
    if not head or not k:
        
        return None
    
    fast=head
    slow=head
    
    for _ in range(k):
         
        if fast is not None:
            
            fast=fast.next
        
    while fast:
        
        slow=slow.next
        fast=fast.next
        
    return slow

def print_list(head):
    
    curr=head
    while curr:
        
        print(curr.val , end=" ")
        curr=curr.next
        
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    arr = [1, 2, 3, 4, 5]
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    print("Original Linked List:")
    print_list(head)
    
    # Find the 2nd node from the end
    k = 2
    result = kth_element_from_last(head, k)
    
    if result:
        print(f"The {k}th node from the end has value: {result.val}")
    else:
        print(f"There is no {k}th node from the end in the list.")