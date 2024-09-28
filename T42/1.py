# You are given an array 'arr' of length 'n', consisting of integers.



# A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.



# Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.



# The sum of an empty subarray is 0.



def maximum_subarray_sum(array):
    
    n=len(array)
    max_lenght = float('-inf')

    for start in range(n):
        
        current= 0
        for end in range(start,n):
            
            current += array[end]

            if current > max_lenght:
                
                max_lenght=current
                
                node=array[start:end+1]
                
    return max_lenght , node
            
            

arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
print(maximum_subarray_sum(arr))
