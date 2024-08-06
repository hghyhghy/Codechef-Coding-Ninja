
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

def moving_zeroes(array):
    
    unique_index=0
    
    for i in range(len(array)):
        
        if array[i] != 0:
            
            array[unique_index]= array[i]

            unique_index += 1
            
    for i in range(unique_index,len(array)):
        
        array[i] = 0
            
    return array

nums = [0,1,0,3,12]
print(moving_zeroes(nums))