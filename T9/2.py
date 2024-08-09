# Length of the longest subarray with zero Sum

def largest_subarray_with_zero_sum(array):
    
    n=len(array)
    max_length = 0 
    
    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum ==  0:
                
                max_length=max(max_length,end-start+1)

    return max_length

arr = [1, -1, 3, 2, -2, -3, 1]
print(largest_subarray_with_zero_sum(arr))
        
        