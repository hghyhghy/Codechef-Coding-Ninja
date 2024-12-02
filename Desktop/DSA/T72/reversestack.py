# Problem statement
# Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input parameter itself.



# Note: You are not allowed to use any extra space other than the internal stack space used due to recursion.

def reverse_stack(stack:list[int])->list[int]:
    
    temp=[]
    
    while stack:
        
        temp.append(stack.pop())
        
    return temp

stack = [1, 2, 3, 4, 5]
print(reverse_stack(stack))