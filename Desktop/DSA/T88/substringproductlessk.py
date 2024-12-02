# Problem statement
# You are given an array ‘ARR’ consist of ‘N’ positive integers, and a positive integer ‘K’.

# Your task is to count and return the number of contiguous subarrays having products of their elements strictly less than ‘K’.

# Example:

# Consider an array ARR = [1, 2, 3, 4, 5], and K = 7, then all the subarrays having product less than 7 are  [1], [2], [3], [4], [5], [1, 2], [2,3], [1,2,3]   i.e there is total 8 subarays having product less than 7.

def subarray_count_less_than_k(array:list[int],k:int)->int:
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        product= 1
        
        for j in range(i,n):
            
            product *= array[j]
            
            if product < k:
                
                count += 1
                
            else:
                
                break
                
    return count

arr = [1, 2, 3, 4, 5]
k = 7
print(subarray_count_less_than_k(arr,k))