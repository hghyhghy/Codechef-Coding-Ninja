# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#using optimal approach 

def minimum_length_of_subarray(array,target):
    
    n=len(array)
    minimum=float("inf")
    start = 0
    current  =0
    
    
    for end in range(n):
        
        current += array[end]

        while current >= target:
            
            minimum =min(minimum,end-start+1)

            current -= array[start]
            start += 1
            
    return minimum

nums = [2, 3, 1, 2, 4, 3]
target = 7

print(minimum_length_of_subarray(nums,target))