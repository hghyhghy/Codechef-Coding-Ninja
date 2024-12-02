# Problem statement
# Design a data structure to implement deque of size ‘N’. It should support the following operations:

# pushFront(X): Inserts an element X in the front of the deque. Returns true if the element is inserted, otherwise false.

class Deque:
    
    def __init__(self):
        
        self.queue=[]

    def is_empty(self)-> bool:
        
        return len(self.queue) == 0
    
    def add_front(self,item):
        
        self.queue.insert(0,item)

    def add_rear(self,item):
        
        self.queue.append(item)

    def remove_front(self):
        
        if not self.is_empty():
            
            return self.queue.pop(0)

    def remove_rear(self):
        
        if not self.is_empty():
            
            return self.queue.pop()

    
    def size(self) ->int:
        
        return len(self.queue)

    
    def peek_front(self):
        
        if not self.is_empty():
            
            return self.queue[0]

    def peek_rear(self):
        
        if not self.is_empty():
            
            return self.queue[-1]

deque = Deque()
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
print(deque.queue)  # Output: [0, 1, 2]
print(deque.remove_front())  # Output: 0
print(deque.remove_rear())   # Output: 2
print(deque.queue)