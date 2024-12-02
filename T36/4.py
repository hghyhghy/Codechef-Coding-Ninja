# Problem statement
# You are given an array “arr'' of integers. Your task is to find the contiguous subarray within the array which has the largest product of its elements. You have to report this maximum product.

# An array c is a subarray of array d if c can be obtained from d by deletion of several elements from the beginning and several elements from the end.

# For e.g.- The non-empty subarrays of an array [1,2,3] will be- [1],[2],[3],[1,2],[2,3],[1,2,3]. 
# For Example:
# If arr = {-3,4,5}.
# All the possible non-empty contiguous subarrays of “arr” are {-3}, {4}, {5}, {-3,4}, {4,5} and {-3,4,5}.
# The product of these subarrays are -3, 4, 5, -12, 20 and -60 respectively.
# The maximum product is 20. Hence, the answer is 20

def maximum_product_subarray(array):
    
    n=len(array)
    max_product=float('-inf')

    for start in range(n):
        
        product= 1
        
        for end in range(start,n):
            
            product *= array[end]

            max_product = max(max_product,product)

    return max_product

arr = [2, 3, -2, 4]

print(maximum_product_subarray(arr))