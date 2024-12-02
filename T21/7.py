

# reversing a stack 

class Stack:

    def __init__(self):

        self.items=[]

    def is_empty(self):

        return len(self.items) == 0
    
    def push(self,item):

        self.items.append(item)

    def pop(self):

        if not self.is_empty():

            return self.items.pop()
        
        else:

            return None
        
    def peek(self):

        if not self.is_empty():

            return self.items[-1]
        else:

            return None
        
    def size(self):

        return len(self.items)

    def __str__(self):

        return str(self.items)

def reverse_stack(original):

        temp=Stack()

        while not original.is_empty():

            temp.push(original.pop())
        
        return temp
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print("Original stack:")
    print(stack)

    reverse=reverse_stack(stack)
    print("Reversed stack:")
    print(reverse)

    