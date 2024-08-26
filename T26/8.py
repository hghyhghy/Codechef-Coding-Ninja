# Problem statement
# You are given an array 'arr' of length 'n', consisting of integers.



# A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.



# Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.



# The sum of an empty subarray is 0.


def maximum_subarray_sum(arr):
    
    n=len(arr)
    max_sum=float('-inf')

    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += arr[end]
            max_sum = max(max_sum,current_sum)

    return max_sum

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(arr))