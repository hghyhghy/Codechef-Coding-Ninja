# Problem statement
# Given an array ‘ARR’ and an integer ‘K’, your task is to find all the count of all sub-arrays whose sum is divisible by the given integer ‘K’.

# Note:
# If there exists no subarray in the given sequence whose sum is divisible by ‘K’ then simply return ‘0’.
# Example:
# Suppose the given array is ‘ARR’ = { 5, 0, 2, 3, 1} and ‘K = 5’.
# As we can see in below image, there are a total of 6 subarrays that have the total sum divisible by ‘K’
# So we return the integer 6.

def subarray_sum_divisible_by_k(array,k):
    
    n=len(array)
    count = 0
    
    for start in range(n):
        
        current_sum= 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum % k == 0:
                
                count += 1
                
    return count

arr = [4, 5, 0, -2, -3, 1]
K = 5

print(subarray_sum_divisible_by_k(arr,K))