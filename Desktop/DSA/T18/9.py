# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

def product_subarray_less_than_k(array,target):
    
    count= 0
    n=len(array)


    for start in range(n):
        
        product = 1
        
        for end in range(start,n):
            
            product *= array[end]
            
            if product < target:
                
                count += 1
                
            else:
                
                break
            
    return count

nums = [10, 5, 2, 6]
k = 100

print(product_subarray_less_than_k(nums,k))
            