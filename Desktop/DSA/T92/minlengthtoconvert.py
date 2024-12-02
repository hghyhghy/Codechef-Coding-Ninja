# Problem statement
# You are given an array of size ‘n’ to find the minimum number of steps to either convert it into either non-decreasing or non-increasing array. In one step you can either increment or decrement the element of the array.
def min_length_to_convert(array:list[int])->int:
    
    n=len(array)

    non_decrease=0
    
    for i in range(1,n):
        
        if array[i]<array[i-1]:
            
            non_decrease += array[i-1]-array[i]

    
    non_increae=0
    
    for  i in range(1,n):
        
        if array[i]>array[i-1]:
            
            non_increae += array[i]-array[i-1]
            
    
    return min(non_decrease,non_increae)

arr = [3, 1, 2, 5, 4]
print(min_length_to_convert(arr))