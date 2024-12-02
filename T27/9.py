# Problem statement
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.



# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.



# Given the array [-5, -1, -8, -9], the maximum sum would be -1.


def min_subarray_sum(arr):
    
    n=len(arr)

    min_sum=float('inf')

    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += arr[end]

            min_sum = min(min_sum,current_sum)

    return min_sum

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(min_subarray_sum(arr))
