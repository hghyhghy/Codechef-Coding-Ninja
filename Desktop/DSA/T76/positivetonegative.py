# You are given an array 'ARR' consisting of 'N' integers. You need to rearrange the array elements such that all negative numbers appear before all positive numbers.

# Note:
# The order of elements in the resulting array is not important.
# Example:
# Let the array be [1, 2, -3, 4, -4, -5]. On rearranging the array such that all negative numbers appear before all positive numbers we get the resulting array [-3, -5, -4, 2, 4, 1].

def negative_to_positive(array:list[int])->list[int]:
    
    n=len(array)
    ngative=[]
    positive=[]
    
    for num in array:
        
        if num > 0:
            
            positive.append(num)
            
        else:
            
            ngative.append(num)
            
    tmp=ngative +positive
    
    for i in range(n):
        
        array[i] =  tmp[i]
        
    return array

arr = [1, 2, -3, 4, -4, -5]
print(negative_to_positive(arr))
