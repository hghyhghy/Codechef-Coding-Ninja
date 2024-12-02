# Problem statement
# Stack is a data structure that follows the LIFO (Last in First out) principle. Design and implement a stack to implement the following functions:

# 1. Push(num): Push the given number in the stack if the stack is not full.

# 2. Pop: Remove and print the top element from the stack if present, else print -1.

# 3. Top: Print the top element of the stack if present, else print -1.

# 4. isEmpty: Print 1 if the stack is empty, else print 0.

# 5. isFull: Print 1 if the stack is full, else print 0.


# You have been given ‘m’ operations which you need to perform in the stack. Your task is to implement all the functions of the stack.

class Stack:
    
    def __init__(self):
        
        self.items=[]
        
    def is_empty(self):
        
        return len(self.items) == 0
    
    
    def push(self,x):
        
        self.items.append(x)
        
    
    def pop(self):
        
        if self.is_empty():
            
            return "Stack is empty"
        
        return self.items.pop()
    
    def peek(self):
        
        if self.is_empty():
            
            return "stack is empty"
        
        return self.items[-1]
    
    def size(self):
        
        return len(self.items)
    
    def display(self):
        # Print the stack from top to bottom
        print("Stack from top to bottom:", self.items[::-1])

# Example usage
s = Stack()

s.push(1)
s.push(2)
s.push(3)

s.display()  # Output: Stack from top to bottom: [3, 2, 1]

print("Top element:", s.peek())  # Output: Top element: 3

print("Popped element:", s.pop())  # Output: Popped element: 3

s.display()  # Output: Stack from top to bottom: [2, 1]

print("Is stack empty?", s.is_empty())  # Output: Is stack empty? False

print("Size of stack:", s.size())