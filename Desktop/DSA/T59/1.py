# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

def contigous_array(array):
    
    n=len(array)
    max_length=0
    
    for start in range(n):
        
        zero=0
        one=0
        
        for end in range(start,n):
            
            if array[end] ==0:
                
                zero += 1
                
            else:
                
                one += 1
                
            if zero==one:
                
                max_length=max(max_length,end-start+1)
            
    return max_length

nums = [0, 1, 0, 1, 0, 1]
print(contigous_array(nums))
