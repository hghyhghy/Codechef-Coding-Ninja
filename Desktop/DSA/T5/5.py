# Problem Statement: Given the head of a linked list, print the length of the linked list.

class Node:
    
    def __init__(self,val=0,next=None):
        
        self.val=val
        self.next=next
        
        
def finding_length(head):
    
    current = head
    count=0
    
    while current:
        
        count += 1
        current = current.next 
        
    
    return count


if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3
    arr = [1, 2, 3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])

      # Element to be checked for presence in the linked list

    # Call the check_if_present function and print the result
    print(finding_length(head))
        