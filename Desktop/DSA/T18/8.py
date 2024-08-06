# 628. Maximum Product of Three Numbers
# Easy
# Topics
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

def maximum_product_of_three_numbers(array):
    
    max_count=float('-inf')
    n=len(array)

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                product = array[i]*array[j]*array[k]

                max_count = max(max_count,product)

    return max_count

nums = [-10, -10, 5, 2]
print(maximum_product_of_three_numbers(nums))