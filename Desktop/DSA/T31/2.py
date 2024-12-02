# Problem statement
# Implement a Queue Data Structure specifically to store integer data using a Singly Linked List or an array.

# You need to implement the following public functions :

from collections import deque

class Queue:
    
    def __init__(self):
        
        self.queue=deque()

    
    def is_empty(self):
        
        return len(self.queue) == 0
    
    def enqueue(self,item):
        
        self.queue.append(item)

    
    def dequeue(self):
        
        if self.is_empty():
            
            return "No elements"

        return self.queue.popleft()

    def peek(self):
        
        if self.is_empty():
            
            return None
        
        return self.queue[0]

    
    def size(self):
        
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2
print(q.is_empty()) 