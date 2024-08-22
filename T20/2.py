# 974. Subarray Sums Divisible by K
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

def subarray_sum_divisible_by_k(array,k):
    
    count= 0
    n=len(array)

    for start in range(n):
        
        total_sum = 0
        
        for end in range(start,n):
            
            total_sum += array[end]

            if total_sum % k == 0:
                
                count += 1
                
    return count

nums = [4, 5, 0, -2, -3, 1]
k = 5

print(subarray_sum_divisible_by_k(nums,k))