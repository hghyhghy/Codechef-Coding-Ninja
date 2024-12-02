
from queue import Queue

class Stackusingqueue:
    
    def __init__(self):
        
        self.q=Queue()
     
    def Empty(self):
        
        return self.q.empty()
    
    def push(self,x):
        
        self.q.put(x)

        size=self.q.qsize()
        
        for _ in range(size-1):
            
            self.q.put(self.q.get())

    def pop(self):
        
        if not self.Empty():
            
            return self.q.get()

        return None
    
    def peek(self):
        
        if not self.Empty():
            
            return self.q.queue[0]

        return None

stack = Stackusingqueue()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())   # Output: 3 (Last pushed element)
print(stack.pop())   # Output: 3 (Remove last pushed element)
print(stack.peek())   # Output: 2 (Now the last pushed element)
print(stack.Empty())
        