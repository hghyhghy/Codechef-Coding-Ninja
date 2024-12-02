# Problem statement
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.



# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.



# Given the array [-5, -1, -8, -9], the maximum sum would be -1.

def maximum_subarray_array(array):
    
    n=len(array)
    max_sum=float("-inf")
    
    for start in range(n):
        
        current = 0
        
        for end in range(start,n):
            
            current += array[end]
            
            if current > max_sum:
                
                subarray=array[start:end+1]
                max_sum =current
                
    return subarray,max_sum

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_array(arr))