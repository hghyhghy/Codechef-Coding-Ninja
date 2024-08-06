# 217. Contains Duplicate
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_dupliate(arr):
    
    count={}

    for num in arr:
        
        if num  in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
            
            
    for cnt in count.values():
        
        if cnt > 1:
            
            return True
        
        
    return False

nums = [1,2,3,4]
print(contains_dupliate(nums))