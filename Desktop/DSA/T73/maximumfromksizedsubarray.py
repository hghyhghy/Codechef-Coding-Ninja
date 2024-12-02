# You are given an array “A” of N integers. Your task is to find the maximum element in all K sized contiguous subarrays from left to right.

# For Example:
# If A = [3, 2, 3], and K = 2.
# Then max of [3, 2] = 3 and max of [2, 3] = 3
# So, the answer will be [3, 3]

# If A = [3, 2, 3, 5, 1, 7] and K = 3.
# Then max of [3, 2, 3] = 3 
# Then max of [2, 3, 5] = 5 
# Then max of [3, 5, 1] = 5 
# Then max of [5, 1, 7] = 7 
# So  the answer will be [3, 5, 5, 7]
from typing import List
def maximum_from_k_sized_subarray(array:List[int],k:int)->List[int]:
    
    n=len(array)
    result=[]
    
    for i in range(n-k+1):
        
        subarray=array[i:i+k]
        
        maximum= max(subarray)
        
        result.append(maximum)
        
    return result

A = [3, 2, 3, 5, 1, 7]
K = 3

print(maximum_from_k_sized_subarray(A,K))