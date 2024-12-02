
# Code


# Testcase
# Test Result
# Test Result
# 713. Subarray Product Less Than K
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

def subarray_product_less_than_k(array,k):
    
    n=len(array)
    count= 0
    
    for start in range(n):
        
        product = 1
        
        for end in range(start,n):
            
            product *= array[end]

            if product < k:
                
                count += 1
                
            else:
                
                break
    
    return count

nums = [10, 5, 2, 6]
k = 100
print(subarray_product_less_than_k(nums,k))