# 152. Maximum Product Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

def maximum_product_subarray(array):
    
    n=len(array)
    max_product =float("-inf")
    
    for start in range(n):
        
        product=1
        
        for end in range(start,n):
            
            product *= array[end]
            max_product=max(max_product,product)

    return max_product

nums = [2,3,-2,4]
print(maximum_product_subarray(nums))