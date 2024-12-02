# Problem statement
# You are given an array 'ARR' of integers of length 'N' and a positive integer 'K'. You need to find the maximum elements for each and every contiguous subarray of size K of the array.

def max_of_subarray_with_size_k(array,k):
    
    n=len(array)
    if n < k or not array:
        
        return 
    
    result = []

    for start in range(n-k+1):
        
        max_value =  array[start]

        for end in range(start,start+k):
            
            if array[end] > max_value:
                
                max_value =  array[end]
        
        result.append(max_value)

    return result

arr = [3, 4, -1, 1, 5]
k = 3

print(max_of_subarray_with_size_k(arr,k))