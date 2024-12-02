# 287. Find the Duplicate Number
# Medium
# Topics
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

def finding_duplicates(nums):
    
    count = {}
    for num in nums:
        
        if num in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
            
    for num,freq in count.items():
        
        if  freq > 1:
            
            return num
        
    return 0

nums = [1,3,4,2,2]
print(finding_duplicates(nums))