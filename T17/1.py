# 219. Contains Duplicate II
# Easy
# Topics
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def contains_duplicate_two(array,k):
    
    hash_map={}

    for  i , num in enumerate(array):
        
        if num in hash_map:
            
            if i - hash_map[num] <= k:
                
                return True
            
        hash_map[num] = i
        
    return False

nums = [1,2,3,1]
k = 3
print(contains_duplicate_two(nums,k))