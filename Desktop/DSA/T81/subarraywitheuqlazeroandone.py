# Problem statement
# You are given an array consisting of 0s and 1s. You need to find the length of the largest subarray with an equal number of 0s and 1s.

# For example:

# If the given array is: [0, 0, 1, 0, 1] The largest subarray would be: [0, 1, 0, 1] (last 4 elements) having length 4.

def largest_subarray_with_equal_zero_one(array:list[int])->int:
    
    n=len(array)
    max_len = float("-inf")

    for i in range(n):
        
        count_zero = 0
        count_one = 0
        
        for j in range(i,n):
            
            if array[j] ==  0:
                
                count_zero += 1
                
            if array[j] == 1:
                
                count_one += 1
                
            if count_one == count_zero:
                
                max_len =max(max_len,j-i+1)
                
    return max_len

arr = [0, 0, 1, 0, 1]
print(largest_subarray_with_equal_zero_one(arr))