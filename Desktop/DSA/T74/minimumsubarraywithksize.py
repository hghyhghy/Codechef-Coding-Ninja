# You have been given an array 'ARR' of integers consisting of ‘N’ integers and a positive integer ‘K’. Your task is to find a subarray(contiguous) of size ‘K’ such that the sum of its elements is minimum.

# Note :
# You can assume that the value of ‘K’ will always be less than or equal to ‘N’. So, the answer will always exist. use brute force approach 

def minimum_subarray_k_size(array:list[int],k:int)->int:
    
    n=len(array)
    min_len=float("inf")
    
    for i in range(n-k+1):
        
        current =sum(array[i:i+k])
        
        if current < min_len:
            
            min_len =  current
            
    return min_len

N = 7
K = 3
ARR = [2, 1, 5, 1, 3, 2, 1]
print(minimum_subarray_k_size(ARR,K))