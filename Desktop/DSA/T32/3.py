# Problem statement
# You are given an integer array 'arr' of size 'N' and an integer 'K'.

# Your task is to find the total number of subarrays of the given array whose sum of elements is equal to k.

# A subarray is defined as a contiguous block of elements in the array.

# Example:
# Input: ‘N’ = 4, ‘arr’ = [3, 1, 2, 4], 'K' = 6

def subarray_with_given_sum(array,target):
    
    n=len(array)

    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum ==  target:
                
                return (start,end)

    return (-1,-1)

arr = [1, 2, 3, 7, 5]
target_sum = 12

print(subarray_with_given_sum(arr,target_sum))