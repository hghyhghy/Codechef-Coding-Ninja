# Problem statement
# You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to sort this array/list. Think of a solution which scans the array/list only once and don't require use of an extra array/list.

# Note:
# You need to change in the given array/list itself. Hence, no need to return or print anything. 

def sorting_binary_array(array):
    
    left=0
    right=len(array)-1
    current= 0
    
    while current <= right:
        
        if array[current] == 0:
            
            array[left],array[current]=  array[current],array[left]

            left += 1
            current += 1
            
            
        else:
            
            array[right],array[current]= array[current],array[right]
            right -= 1
            
            
    return array
arr = [0, 1, 1, 0, 1, 0, 0, 1]

print(sorting_binary_array(arr))