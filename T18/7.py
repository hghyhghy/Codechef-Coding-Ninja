# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subarray_equal_to_sum_k(array,target):
    
    count=0
    n=len(array)

    for start in range(n):
        
        total_sum = 0
        
        for end in range(start,n):
            
            total_sum += array[end]

            if  total_sum == target:
                
                count += 1
                
    return count

nums = [1,1,1]
k = 2
print(subarray_equal_to_sum_k(nums,k))