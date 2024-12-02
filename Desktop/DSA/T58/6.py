# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def max_consecutive_ones(array):
    
    n=len(array)
    max_lenght=float("-inf")
    count =0
    for i in range(n):
        
        if array[i] == 1:
            
            count += 1
            
        else:
            
            max_lenght =max(max_lenght,count)
            count= 0
            
    max_lenght=max(max_lenght,count)

    return max_lenght

nums = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(nums))