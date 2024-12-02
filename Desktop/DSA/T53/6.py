# Medium
# Topics
# Companies
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

def maximum_product_subarray(array):
    
    n=len(array)
    max_product = float("-inf")

    for start in range(n):
        
        product =1
        
        for end in range(start,n):
            
            product *= array[end]

            if product>max_product:
                
                max_product=product
                result=array[start],array[end]
                
    return max_product,result

nums = [2, 3, -2, 4]
print(maximum_product_subarray(nums))