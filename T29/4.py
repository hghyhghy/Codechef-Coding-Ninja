# Problem statement
# You have been given an array 'ARR' of integers consisting of ‘N’ integers and a positive integer ‘K’. Your task is to find a subarray(contiguous) of size ‘K’ such that the sum of its elements is minimum.

# Note :
# You can assume that the value of ‘K’ will always be less than or equal to ‘N’. So, the answer will always exist

def min_subarray_sub_with_k(arr,k):
    
    n=len(arr)

    if k>n:
        
        return None
    
    min_value=float('inf')

    for i in range(n-k+1):
        
        total_sum=0
        
        for j in range(i,i+k):
            
            total_sum += arr[j]

        min_value = min(min_value,total_sum)

    
    return min_value

arr = [2, 1, 5, 1, 3, 2]
k = 3

print(min_subarray_sub_with_k(arr,k))
    
    