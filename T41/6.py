# Problem statement
# You have been given an array(ARR) of positive integers and an integer X. You have to find the minimum length subarray such that the sum of all of its elements is strictly greater than the given integer X.

# Note:
# A subarray is a contiguous block of elements that can be formed by deleting some (possibly zero) elements from the beginning or the end of the original array. 
# For example :
# If the given array is [1, 2, 3, 4, 5], then [2, 3, 4], [1, 2], [5] are some subarrays while [1, 3], [2, 3, 5] are not.

# If there are multiple subarrays with minimum length, find one which appears earlier in the array (i.e. subarray that starts with lower index).

# If there is no such subarray, print an empty line.

def minimum_subarray_sum(array,target):
    
    n=len(array)
    lenght=float('inf')

    for  start in range(n):
        
        current = 0
        
        for end in  range(start,n):
            
            current += array[end]

            if current >= target:
                
                custom_lenght= end-start+1
                
                lenght= min(lenght,custom_lenght)

    return lenght

arr = [2, 3, 1, 2, 4, 3]
target = 7

print(minimum_subarray_sum(arr,target))