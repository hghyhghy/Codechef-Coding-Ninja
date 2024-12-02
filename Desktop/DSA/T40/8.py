# Problem statement
# Ninjas has been given an array. He wants to find a subarray such that the sum of all elements in the subarray is maximum.

# Subarray 'A' is greater than sub-array 'B' if sum(A) > sum(B). If two sub-array have the same maximum sum, then output the subarray that has a larger length.

# A subarray means a contiguous part of an array. For example, In 'arr' = [1, 2, 3, 4], [1, 2], [2, 3, 4] are the contiguous subarry but [1, 3, 4] is not a subarray.

# Note:

# More than one sub-array can have a maximum sum, in that case, output any.

def max_subarray_sum(array):
    
    n=len(array)
    max_sum=float('-inf')

    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            max_sum=max(current_sum,max_sum)

    return max_sum

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]

print(max_subarray_sum(arr))