# Problem statement
# You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.

# You don't need to print or return anything, just change in the input array itself.

def swap_alternartive(array:list[int])->list[int]:
    
    n=len(array)
    
    for i in range(0,n-1,2):
        
        array[i],array[i+1]=array[i+1],array[i]
        
    
    return array

arr = [1, 2, 3, 4, 5, 6]
print(swap_alternartive(arr))