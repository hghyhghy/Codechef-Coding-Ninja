# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of

def subarray_constigous(array,k):
    
    n=len(array)

    for end in range(n):
        
        temp  = 0

        for start in range(end-1,-1,-1):
            
            temp += array[end]

            if temp % k== 0:
                
                return True
            
            if end-start+1 >=2:
                
                break
            
    return False

nums = [23, 2, 4, 6, 7]
k = 6

print(subarray_constigous(nums,k))
