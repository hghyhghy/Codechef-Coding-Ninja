# Implement a Stack Data Structure specifically to store integer data using two Queues.



# There should be two data members, both being Queues to store the data internally. You may use the inbuilt Queue.



# Implement the following public functions :

# 1. Constructor:
# It initializes the data members(queues) as required.

# 2. push(data) :
# This function should take one argument of type integer. It pushes the element into the stack and returns nothing.

from collections import deque

class Stackusingqueue:
    
    def __init__(self):
        
        self.queue1=deque()
        self.queue2=deque()
        
    def is_empty(self):
        
        return not self.queue1

    def push(self,x):
        
        self.queue2.append(x)

        while self.queue1:
            
            self.queue2.append(self.queue1.popleft())
            
        self.queue1,self.queue2=self.queue2,self.queue1
    
    
    def top(self):
        
        if not self.is_empty():
            
            return self.queue1[0]

    def pop(self):
        
        if not self.is_empty():
            
            return self.queue1.popleft()


stack = Stackusingqueue()
stack.push(1)
stack.push(2)
stack.push(3)
    
print(stack.top())   # Output: 3
print(stack.pop())   # Output: 3
print(stack.top())   # Output: 2
print(stack.pop())   # Output: 2
print(stack.is_empty()) # Output: False
print(stack.pop())   # Output: 1
print(stack.is_empty())