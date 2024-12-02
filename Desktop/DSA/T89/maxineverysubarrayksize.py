# Problem statement
# Given an array/list of integers of length ‘N’, there is a sliding window of size ‘K’ which moves from the beginning of the array, to the very end. You can only see the ‘K’ numbers in a particular window at a time. For each of the 'N'-'K'+1 different windows thus formed, you are supposed to return the maximum element in each of them, from the given array/list.

def max_in_subarray_of_size_k(array:list[int],k:int)->list[int]:
    
    n=len(array)
    result= []

    for start in range(n-k+1):
        
        maximum = array[start]
        
        for end in range(start,start+k):
            
            if array[end] > maximum:
                
                maximum = array[end]
                
        result.append(maximum)

    
    return result

arr = [1, 3, -1, -3, 5, 3, 6, 7]
N = len(arr)
K = 3

print(max_in_subarray_of_size_k(arr,K))