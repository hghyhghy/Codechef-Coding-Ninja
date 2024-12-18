# Problem statement
# Given an array 'arr' containing 'n' elements, rotate this array left once and return it.



# Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.



# Example:
# Input: 'a' = 5, 'arr' = [1, 2, 3, 4, 5]

# Output: [2, 3, 4, 5, 1]

# Explanation: We moved the 2nd element to the 1st position, and 3rd element to the 2nd position, and 4th element to the 3rd position, and the 5th element to the 4th position, and move the 1st element to the 5th position.

def left_array_by_one(array):
    
    n=len(array)
    if n ==0 :
        
        return None
    
    first_number=array[0]

    for  i in range(n):
        
        array[i-1]= array[i]

    array[-1] =  first_number
    
    return array

arr = [1, 2, 3, 4, 5]
print(left_array_by_one(arr))