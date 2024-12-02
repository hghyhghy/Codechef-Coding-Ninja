# Problem statement
# Implement a queue data structure which follows FIFO(First In First Out) property, using only the instances of the stack data structure.



# Note:
# 1. To implement means you need to complete some predefined functions, which are supported by a normal queue such that it can efficiently handle the given input queries which are defined below.

class Queue:
    
    def __init__(self):
        
        self.q1=[]
        self.q2=[]
        
    def enQueue(self,x):
        
        self.q1.append(x)
        
    def isEmpty(self):

        return len(self.q1) == 0 and len(self.q2) ==0
    
    def deQueue(self):
        
        if self.isEmpty():
            
            return -1
        
        
        if not self.q2:
            
            while  self.q1:
                
                self.q2.append(self.q1.pop())
        
        return self.q2.pop()


    
    def peek(self):
        
        if self.isEmpty():
            
            return -1
        
        if not self.q2:
            
            while self.q1:
                
                self.q2.append(self.q1.pop())

        
        return self.q2[-1]
    
if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enQueue(10)
    queue.enQueue(20)
    queue.enQueue(30)

    # Peek the front element
    print("Front element:", queue.peek())  # Output: 10

    # Dequeue elements
    print("Dequeue element:", queue.deQueue())  # Output: 10
    print("Dequeue element:", queue.deQueue())  # Output: 20

    # Peek after dequeuing some elements
    print("Front element after dequeuing:", queue.peek())  # Output: 30

    # Check if queue is empty
    print("Is queue empty?", queue.isEmpty())  # Output: False

    # Dequeue remaining elements
    print("Dequeue element:", queue.deQueue())  # Output: 30
    print("Is queue empty?", queue.isEmpty())  # Output: True

    # Try to dequeue from an empty queue
    print("Dequeue from empty queue:", queue.deQueue())  # Output: Queue is empty!
