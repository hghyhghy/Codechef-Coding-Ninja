
# Code
# Testcase
# Test Result
# Test Result
# 704. Binary Search
# Easy
# Topics
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

def binary_search(array,target):

    left=0
    right=len(array)-1
    
    while left <= right:
        
        mid=(left+right)//2 
        
        if array[mid] == target:
            
            return mid
        
        elif array[mid] <  target:
            
            left = mid + 1
            
        else:
            
            right = mid-1
            
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(binary_search(nums,target))