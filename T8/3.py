# implement stack using queue

class Newstack:
    
    def __init__(self):
        
        self.queue=[]

    def is_empty(self):
        
        return len(self.queue) == 0

    def push(self,item):
        
        self.queue.append(item)

        for _ in range(len(self.queue)-1):
            
            self.queue.append(self.queue.pop(0))

    def pop(self):
        
        if self.is_empty():
            
            return "Queue is empty"

        return self.queue.pop(0)

    def top(self):
        
        if self.is_empty():
            
            return "Queue is empty"
        
        return self.queue[0]

    def size(self):
        
        return len(self.queue)

    def __str__(self):

        return str(self.queue)

stack=Newstack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())    # Output: 3
print(stack.pop())    # Output: 3
print(stack.size())   # Output: 2
print(stack)   
        