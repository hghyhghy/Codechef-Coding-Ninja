# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def product_of_array_except_self(array):
    
    n=len(array)
    dp=[1]*n
    
    for i in range(n):
        
        product=1
        
        for j in range(n):
            
            if array[i] != array[j]:
                
                product *= array[j]
        dp [i] = product

    return dp
nums = [1,2,3,4]
print(product_of_array_except_self(nums))