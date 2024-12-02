# You are given an array ‘arr’, your task is to find an element, such that it is strictly larger than its left and right neighbour and return its index in the array.

# Note:
# Assume that the first and the last element of the array is -∞. 
# For Example:
# You are given ‘arr’ = [4, 6, 3, 2], Here element 6 is greater than 4 as well as 3, the index of 6 is 1. Hence the answer is 1.

def peak_element(array:list[int])->int:
    
    n=len(array)
    if n==1:
        
        return 0
    
    if array[0]>array[1]:
        
        return  0
    
    if array[n-1]>array[n-2]:
        
        return array[n-1]
    
    for i in range(1,n-1):
        
        if array[i-1]<array[i]>array[i+1]:
            
            return i
        
    return -1

arr = [4, 6, 3, 2]
print(peak_element(arr))