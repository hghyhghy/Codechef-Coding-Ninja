# Problem statement
# Given an array 'arr' containing 'n' elements, rotate this array left once and return it.



# Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.


def left_rotate_by_one(arr):
    
    if len(arr)  == 0:
        
        return None
    
    first_element= arr[0]

    for i in range(len(arr)-1):
        
        arr[i] = arr[i+1]

    
    arr[-1] = first_element
    
    return arr

arr = [1, 2, 3, 4, 5]
print(left_rotate_by_one(arr))