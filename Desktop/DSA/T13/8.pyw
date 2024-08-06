# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

def find_first_last_occurance(nums,target):
    
    start=-1
    end = -1
    
    for i in range(len(nums)):
        
        if nums[i] == target:
            
            start = i
            break
        
    
    for j in range(len(nums)-1,-1,-1):
        
        if nums[j] == target:
            
            end = j
            
            break
        
    return [start,end]

nums = [5, 7, 7, 8, 8, 10]
target = 8

print(find_first_last_occurance(nums,target))