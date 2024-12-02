# Problem statement
# Implement a Stack Data Structure specifically to store integer data using two Queues.



# There should be two data members, both being Queues to store the data internally. You may use the inbuilt Queue.



# Implement the following public functions :

# 1. Constructor:
# It initializes the data members(queues) as required.

# 2. push(data) :
# This function should take one argument of type integer. It pushes the element into the stack and returns nothing.

# 3. pop() :
# It pops the element from the top of the stack and, in turn, returns the element being popped or deleted. In case the stack is empty, it returns -1.

# 4. top :
# It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.

# 5. size() :
# It returns the size of the stack at any given instance of time.

# 6. isEmpty() :
# It returns a boolean value indicating whether the stack is empty or not.
# Operations Performed on the Stack:
# Query-1(Denoted by an integer 1): Pushes an integer data to the stack. (push function)

# Query-2(Denoted by an integer 2): Pops the data kept at the top of the stack and returns it to the caller. (pop function)

# Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the top of the stack but doesn't remove it, unlike the pop function. (top function)

# Query-4(Denoted by an integer 4): Returns the current size of the stack. (size function)

# Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the stack is empty or not. (isEmpty function)

from collections import deque

class Stack:
    
    def __init__(self):
        
        self.q1=deque()
        self.q2=deque()
        
    def get_size(self):
        
        return len(self.q1)

    def is_empty(self):
        
        return len(self.q1) == 0
    
    def push(self,x):
        
        self.q2.append(x)
        
        while  len(self.q1) > 0:
            
            self.q2.append(self.q1.popleft())

        self.q1,self.q2=self.q2,self.q1
        
    
    def pop(self):
        
        if not self.is_empty():
            
            return self.q1.popleft()

    
    def top(self):
        
        if not self.is_empty():
            
            return self.q1[0]
        

if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Current top element:", stack.top())  # Output: 30

    print("Pop element:", stack.pop())  # Output: 30
    print("Current top element:", stack.top())  # Output: 20

    print("Stack size:", stack.get_size())  # Output: 2

    print("Is stack empty?", stack.is_empty())  # Output: False

    print("Pop element:", stack.pop())  # Output: 20
    print("Pop element:", stack.pop())  # Output: 10
    print("Is stack empty?", stack.is_empty())  # Output: True

    print("Pop from empty stack:", stack.pop())  # Output: Stack is empty!