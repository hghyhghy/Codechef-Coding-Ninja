# Problem statement
# Given an array arr of length N consisting of positive and negative integers, return the length of the longest subarray whose sum is zero.

def maX_subarray_with_zero_sum(array):
    
    max_length = float('-inf')
    n=len(array)

    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum == 0:
                
                length = end-start+1
                
                if length > max_length:
                    
                    max_length =  length
                    
    return max_length

arr = [1, 2, -3, 3, 4, -4, 2, -2, 2]
print(maX_subarray_with_zero_sum(arr))