# Implement Queue using Stack

class Queueusingstack:
    
    def __init__(self):
        
        self.stack1=[]
        self.stack2=[]

    def enqueu(self,item):
        
        self.stack1.append(item)

    def is_empty(self):
        
        return not(self.stack1 or self.stack2)

    def dequeue(self):
        
        if self.is_empty():
            
            return "empty"

        if not self.stack2():
            
            while self.stack1:
                
                self.stack2.append(self.stack1.pop())
                
        
        return self.stack2.pop()

    
    def front(self):
        
        if self.is_empty():
            
            return "empty"

        if not self.stack2:
            
            while self.stack1:
                
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]
    
    def size(self):
        
        return len(self.stack1) + len(self.stack2)
    
    def __str__(self):
        # For display purposes, show the elements as they would appear in the queue
        if self.stack2:
            return str(self.stack2[::-1] + self.stack1)
        else:
            return str(self.stack1[::-1])
        

queue=Queueusingstack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.front())   # Output: 1
print(queue.dequeue()) # Output: 1
print(queue.size())    # Output: 2
print(queue) 
