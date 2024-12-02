# Problem statement
# Given an array 'arr' containing 'n' elements, rotate this array left once and return it.



# Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.

def left_rotate_array_by_one(array:list[int])->list[int]:
    
    n=len(array)
    
    if n==1 :
        
        return array
    
    first_moment=array[0]
    
    for i in range(1,n):
        
        array[i-1] = array[i]
        
    array[n-1]=first_moment
    
    return array

arr = [1, 2, 3, 4, 5]
print(left_rotate_array_by_one(arr))