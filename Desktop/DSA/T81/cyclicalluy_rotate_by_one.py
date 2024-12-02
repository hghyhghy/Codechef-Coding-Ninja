# Problem statement
# You are given an integer array of size N. Your task is to rotate the array by one position in the clockwise direction.

# For example :
# If N = 5 and arr[ ] = {1, 2, 3, 4, 5} then output will be 5 1 2 3 4.

# If N = 8 and arr[ ] = {9, 8, 7, 6, 4, 2, 1, 3} then output will be 3 9 8 7 6 4 2 1.

def cyclically_rotate_array_by_one(array:list[int])->list[int]:
    
    n=len(array)

    last=array[-1]
    
    for i in range(n-1,-1,-1):
        
        array[i] = array[i-1]
        
    array[0] = last
    
    return array

arr1 = [1, 2, 3, 4, 5]
print(cyclically_rotate_array_by_one(arr1))