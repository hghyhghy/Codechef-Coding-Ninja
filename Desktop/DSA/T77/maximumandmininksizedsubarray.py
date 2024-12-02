# You are given an array consisting of N integers, and an integer, K. Your task is to determine the total sum of the minimum element and the maximum element of all subarrays of size K.

# Note :

# The array may contain duplicate elements.
# The array can also contain negative integers.
# The size of the array is at least 2.
# There exists at least one such subarray of size k.

def max_and_min_in_k_subarray(array:list[int],k:int)->int:
    
    n=len(array)
    temporary = 0
    
    for start in range(n-k+1):
        
        subarray = array[start:start+k]

        maximum =  max(subarray)
        minimum =  min(subarray)
        
        temporary += maximum +minimum
        
    return temporary

arr = [2, 5, -1, 7, -3, -1, -2]
K = 3
print(max_and_min_in_k_subarray(arr,K))
        