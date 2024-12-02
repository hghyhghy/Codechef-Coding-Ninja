# Problem statement
# Given an array/list 'ARR' of integers and a position ‘M’. You have to reverse the array after that position.

# Example:

# We have an array ARR = {1, 2, 3, 4, 5, 6} and M = 3 , considering 0 
# based indexing so the subarray {5, 6} will be reversed and our 
# output array will be {1, 2, 3, 4, 6, 5}.

def reverse_after_position(arr,position):
    
    if position < 0 or position >= len(arr) -1:
        
        return arr
    
    start=position+1
    end = len(arr) - 1
    
    while start < end:
        
        arr[start],arr[end] = arr[end],arr[start]

        start += 1
        end -= 1
        
    return arr


arr = [1, 2, 3, 4, 5, 6]
M = 3

print(reverse_after_position(arr,M))
    