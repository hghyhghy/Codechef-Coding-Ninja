# You are given an array/list ‘ARR’ of ‘N’ integers. You have to generate an array/list containing squares of each number in ‘ARR’, sorted in increasing order.

# For example :

# Input:
# ‘ARR’ = [-6,-3, 2, 1, 5] 

# If we take a square of each element then the array/list will become [36, 9, 4, 1, 25].
# Then the sorted array/list will be [1, 4, 9, 25, 36].

def squared_elements_of_array(array:list[int])->list[int]:
    
    new_array=[x**2 for x in array]
    
    new_array.sort()
    
    return new_array

arr = [-6, -3, 2, 1, 5]
print(squared_elements_of_array(arr))