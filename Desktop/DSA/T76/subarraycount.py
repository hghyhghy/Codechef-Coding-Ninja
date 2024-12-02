# You are given an integer array 'arr' of size 'N' and an integer 'K'.

# Your task is to find the total number of subarrays of the given array whose sum of elements is equal to k.

# A subarray is defined as a contiguous block of elements in the array.

# Example:
# Input: ‘N’ = 4, ‘arr’ = [3, 1, 2, 4], 'K' = 6

def count_subarray_sum_equal_k(array:list[int],k:int)->int:
    
    count=0
    n=len(array)
    
    for start in range(n):
        
        curr=0
        
        for end in range(start,n):
        
            curr += array[end]
            
            if curr == k:
                
                count +=1
            
    return count

arr = [3, 1, 2, 4]
K = 6
print(count_subarray_sum_equal_k(arr,K))
