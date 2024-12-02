# Problem statement
# You’re given a stack consisting of 'N' integers. Your task is to sort this stack in descending order using recursion.

# We can only use the following functions on this stack S.

# is_empty(S) : Tests whether stack is empty or not.
# push(S) : Adds a new element to the stack.
# pop(S) : Removes top element from the stack.
# top(S) : Returns value of the top element. Note that this function does not remove elements from the stack.
# Note :
# 1) Use of any loop constructs like while, for..etc is not allowed. 
# 2) The stack may contain duplicate integers.
# 3) The stack may contain any integer i.e it may either be negative, positive or zero.

def sort_stack(stack:list[int])->list[int]:
    
    aux_stack=[]
    
    while stack:
        
        temp=stack.pop()
        
        while aux_stack and aux_stack[-1]<temp:
            
            stack.append(aux_stack.pop())
            
        
        aux_stack.append(temp)
    
    return aux_stack

stack = [34, 3, 31, 98, 92, 23]
print(sort_stack(stack))
        
        
        