# Problem statement
# You have been given a sorted array/list 'arr' consisting of ‘n’ elements. You are also given an integer ‘k’.



# Now, your task is to find the first and last occurrence of ‘k’ in 'arr'.



# Note :
# 1. If ‘k’ is not present in the array, then the first and the last occurrence will be -1. 
# 2. 'arr' may contain duplicate elements.

def first_and_last_position_of_an_element(array,target):
    
    first=-1
    last=-1
    
    n=len(array)
    for i in range(n):
        
        if array[i] ==  target:
            
            first=i
            break
        
        
    for j in range(n):
        
        if array[j] ==  target:
            last=j
            
    
    return first,last

a=[0,1,1,5]
print(first_and_last_position_of_an_element(a,1))