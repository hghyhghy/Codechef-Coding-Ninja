# Find the Minimum Value and Its Index in the Array
 

# Problem Description:

# Given an integer array, find the minimum value and its index in the array.

def minimum_value(array):
    
    mini_val = array[0]
    index = None
    
    for i in range(len(array)):
        
        if array[i] < mini_val:
            
            mini_val = array[i]
            index = i
            
    return mini_val,index

a=[5, 2, 4, 1, 3]
print(minimum_value(a))