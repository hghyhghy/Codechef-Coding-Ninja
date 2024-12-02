# Problem statement
# Ninjas has been given an array. He wants to find a subarray such that the sum of all elements in the subarray is maximum.

# Subarray 'A' is greater than sub-array 'B' if sum(A) > sum(B). If two sub-array have the same maximum sum, then output the subarray that has a larger length.

# A subarray means a contiguous part of an array. For example, In 'arr' = [1, 2, 3, 4], [1, 2], [2, 3, 4] are the contiguous subarry but [1, 3, 4] is not a subarray.

# Note:

# More than one sub-array can have a maximum sum, in that case, output any.

def subarray_with_maximum_dum(array:list[int])->list[int]:
    
    n=len(array)
    max_sum = float("-inf")
    result=[]

    for start in range(n):
        
        current  = 0
        
        for end in range(start,n):
            
            current += array[end]
            
            if current > max_sum or (current == max_sum and (end-start+1)>len(result)):
                
                max_sum =  current
                
                result=array[start : end+1]
                
    
    return result
arr = [1, 2, 3, -2, 5]
print(subarray_with_maximum_dum(arr))