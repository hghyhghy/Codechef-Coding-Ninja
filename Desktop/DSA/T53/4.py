# You are given an array/list ARR consisting of N integers. Your task is to find the maximum possible sum of a non-empty subarray(contagious) of this array.

# Note: An array C is a subarray of array D if it can be obtained by deletion of several elements(possibly zero) from the beginning and the end of array D.

# For e.g.- All the non-empty subarrays of array [1,2,3] are [1], [2], [3], [1,2], [2,3], [1,2,3].

def max_subarray_sum(array):
    
    n=len(array)
    max_sum=float("-inf")

    for start in range(n):
        
        current= 0
        for end in range(start,n):
            
            current += array[end]

            if current > max_sum:
                
                max_sum=current
                subarray=array[start:end+1]

    return max_sum,subarray

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))