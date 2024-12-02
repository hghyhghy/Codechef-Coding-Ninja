# Problem statement
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.



# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.



# Given the array [-5, -1, -8, -9], the maximum sum would be -1.

def max_subarray_sum(array:list)->int:
    
    n=len(array)
    max_sum = float("-inf")
    
    for i in range(n):
        
        currrnt= 0
        
        for end in range(i,n):
            
            currrnt += array[end]
            
            max_sum= max(max_sum,currrnt)

    return max_sum if max_sum >0 else -1

a= [34, -50, 42, 14, -5, 86]
print(max_subarray_sum(a))

