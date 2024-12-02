# Given an unsorted array of integers, you have to move the array elements in a way such that all the zeroes are transferred to the end, and all the non-zero elements are moved to the front. The non-zero elements must be ordered in their order of appearance.

# For example, if the input array is: [0, 1, -2, 3, 4, 0, 5, -27, 9, 0], then the output array must be:

# [1, -2, 3, 4, 5, -27, 9, 0, 0, 0].

def move_zero_to_end(array:list[int])->list[int]:
    
    non_zer=[]
    zer=[]
    
    for num in array:
        
        if num == 0:
            
            zer.append(num)
            
        else:
            
            non_zer.append(num)
            
    return non_zer+zer

arr = [0, 1, -2, 3, 4, 0, 5, -27, 9, 0]
print(move_zero_to_end(arr))