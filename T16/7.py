# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

def minimum_size_subarray(array,target):
    
    n=len(array)
    minimum_val=float('inf')

    for start in range(n):
        
        current_sum= 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum >= target:
                
                minimum_val = min(minimum_val,end-start + 1)

    return minimum_val

nums = [2,3,1,2,4,3]
t=7

print(minimum_size_subarray(nums,t))