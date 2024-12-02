
# Code
# Testcase
# Test Result
# Test Result
# 485. Max Consecutive Ones
# Easy
# Topics
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def max_consecutive_ones(array):
    
    n=len(array)
    max_count=0
    count= 0
    
    for num in array:
        
        if num == 1:
            
            count += 1
            
        else:
            
            max_count = max(max_count,count)
            count = 0
            
    max_count = max(max_count,count)
    
    return max_count

nums = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(nums))