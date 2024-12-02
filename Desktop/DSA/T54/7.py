# Given an array arr[] of size n, the task is to print all subarrays in the array which has sum 0
def subarray_with_zero_sum(array):
    
    n=len(array)

    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum == 0:
                
                substring=array[start:end+1]
                
    return substring

arr = [3, 4, -7, 1, 2, -6, 1, 3, -2, -1]
print(subarray_with_zero_sum(arr))