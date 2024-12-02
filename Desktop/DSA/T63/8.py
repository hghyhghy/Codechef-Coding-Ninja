# Problem statement
# You are given an array 'arr' of length 'n', consisting of integers.



# A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.



# Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.



# The sum of an empty subarray is 0.

#using kadanes algorithm 

def subarray_with_max_sum(array):
    
    max_sum = 0
    current = 0
    
    for num in array:
        
        current += num
        
        if current < 0:
            
            current = 0
            
        if current > max_sum:
            
            max_sum = current
            
    return max_sum

arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
print(subarray_with_max_sum(arr))