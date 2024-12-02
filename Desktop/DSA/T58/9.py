# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

def subarray_equal_to_k(array,k):
    
    n=len(array)
    start=0
    count= 0
    current = 0
    
    for end in range(n):
        
        current += array[end]
        
        while current > k and start<=end:
            
            current -= array[start]
            start += 1
            
        if current == k:
            
            count += 1
            
    return count

nums = [1, 1, 1]
k = 2
print(subarray_equal_to_k(nums,k))
        
        