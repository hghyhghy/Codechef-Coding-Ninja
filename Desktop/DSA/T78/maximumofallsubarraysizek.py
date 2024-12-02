# You are given an array consisting of N non-negative integers, and an integer K denoting the length of a subarray, your task is to determine the maximum elements for each subarray of size K.

# Note:
# A subarray is a contiguous subset of an array.

# The array may contain duplicate elements.

# The given array follows 0-based indexing.

# It is guaranteed that there exists at least one subarray of size K.

def max_of_all_subarray(array:list[int],k:int)->list[int]:
    
    n=len(array)
    result=[]
    
    for i in range(n-k+1):
        
        maximum = array[i]
        
        for j in range(i,i+k):
            
            if array[j] > maximum:
                
                maximum = array[j]
                
        result.append(maximum)
    
    return result

arr = [1, 3, 1, 2, 0, 5]
K = 3
print(max_of_all_subarray(arr,K))