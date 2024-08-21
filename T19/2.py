# 560. Subarray Sum Equals K
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subarray_sum_equals_to_k(array,k):
    
    n=len(array)
    count = 0
    
    for start in range(n):
        
        current_sum = 0
        
        for end in  range(start,n):
            
            current_sum += array[end]

            if current_sum == k:
                
                count += 1
                
    return count

nums = [1, 1, 1]
k = 2
print(subarray_sum_equals_to_k(nums,k))