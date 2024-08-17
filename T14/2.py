# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

def largest_subarray(array):
    
    n=len(array)
    max_sum=float('-inf')

    for start in range(n):
        
        total_sum = 0
        
        for end in range(start,n):
            
            total_sum += array[end]

            if total_sum > max_sum:
                
                max_sum = total_sum
                
    return max_sum

nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(largest_subarray(nums))