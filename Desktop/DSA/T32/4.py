# You are given an array 'ARR' consisting of 'N' integers. You need to rearrange the array elements such that all negative numbers appear before all positive numbers.

# Note:
# The order of elements in the resulting array is not important.
# Example:
# Let the array be [1, 2, -3, 4, -4, -5]. On rearranging the array such that all negative numbers appear before all positive numbers we get the resulting array [-3, -5, -4, 2, 4, 1].

def moving_negative_to_front(array):
    
    n=len(array)
    j =0
    
    for i in range(n):
        
        if array[i] < 0:
            
            array[j],array[i] = array[i],array[j]

            j += 1
            
    return array

s=[1, 2, -3, 4, -4, -5]
print(moving_negative_to_front(s))
