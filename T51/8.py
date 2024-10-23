# Problem statement
# You are given a stack ‘S’. Your task is to sort the sack recursively.



# Note:
# Looping through the stack is not allowed.
# You need to return a stack that is sorted in descending order.

def sort_a_stack(array):

    
    if not array or len(array) ==1:
        
        return array
    
    n=len(array)

    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j] > array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]

    return array

stack = [3, 5, 1, 9, 2, 8]
print(sort_a_stack(stack))