# 643. Maximum Average Subarray I
# Easy
# Topics
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

def maximum_average_subarray(nums,k):
    
    n=len(nums)
    maximum= float('-inf')
    
    for start in range(n-k+1):
        
        current_sum = 0
        
        for end in range(start,start+k):
            
            current_sum += nums[end]

            maximum = max(maximum,current_sum)

    return maximum / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(maximum_average_subarray(nums,k))
    