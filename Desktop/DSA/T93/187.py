


#delete the target node

class ListNode:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        

def main(head,target):
    
    curr=head
    if head == target:
        
        return head.next
    
    while curr.next:
        
        if curr.next.val != target:
            
            curr.next=curr.next.next
            break
        curr=curr.next
            

            
    
    return head

def print_list(head):
    
    curr=head
    while  curr:
        
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
    
    # Remove the 2nd node from the end (which is 4 in this case)
    n = 3
    head = main(head, n)
    
    print("Linked List after removal:")
    print_list(head)
    