# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

def maximum_product_subarray(array):
    
    n=len(array)
    max_product=1
    
    for start in range(n):
        
        product = 1
        
        for end in range(start,n):
            
            product *= array[end]

            max_product = max(max_product,product)

    return max_product

nums = [2,3,-2,4]
print(maximum_product_subarray(nums))