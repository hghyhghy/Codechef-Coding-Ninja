# Given an array ARR of N integers and an integer S. The task is to find whether there exists a subarray(positive length) of the given array such that the sum of elements of the subarray equals to S or not. If any subarray is found, return the start and end index (0 based index) of the subarray. Otherwise, consider both the START and END indexes as -1.

def subarray_with_zero_sum(array,target):
    
    n=len(array)
    max_lenght = float("-inf")

    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum == target:
                
                length = end-start+1
                if length > max_lenght:
                    
                    subarray = array[start:end+1]
                    max_lenght=length
                   

    return subarray,max_lenght

arr = [1, 2, 3, 7, 5]
S = 12

print(subarray_with_zero_sum(arr,S))