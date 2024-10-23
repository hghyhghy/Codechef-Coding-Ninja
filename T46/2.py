# Problem statement
# There is an array ‘A’ of size ‘N’.

# You are also given an integer ‘X’ and direction ‘DIR’. You must rotate the array in the direction of ‘DIR’ by ‘X’ positions.

# You must return the rotated array.

# For example:

def rotate_array(array,x):
    
    n=len(array)
    x=x%n
    
    rotated = array[x:]+ array[:x]
    
    return rotated

arr = [1, 2, 3, 4, 5, 6, 7]
x = 3
print(rotate_array(arr,x))