# Problem statement
# Given an array ARR of N integers and an integer S. The task is to find whether there exists a subarray(positive length) of the given array such that the sum of elements of the subarray equals to S or not. If any subarray is found, return the start and end index (0 based index) of the subarray. Otherwise, consider both the START and END indexes as -1.

# Note:

# If two or more such subarrays exist, return any subarray.
# For Example: If the given array is [1,2,3,4] and the value of S is equal to 7. Then there are two possible subarrays having sums equal to S are [1,2,3] and [3,4].

def subarray_with_given_sum(array:list[int],target:int)->list[int]:
    
    n=len(array)
    
    for i in range(n):
        
        current = 0
        
        for j in range(i,n):
            
            current += array[j]
            
            if current ==  target:
                
                return [i,j]
            
    return [-1,-1]

ARR = [1, 2, 3, 4]
S = 7
print(subarray_with_given_sum(ARR,S))
            
            