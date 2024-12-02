# You are given a sorted integer array 'arr' of size 'n'.



# You need to remove the duplicates from the array such that each element appears only once.



# Return the length of this new array.



# Note:
# Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory. 

def remove_duplicates(array):
    
    n=len(array)
    window=0
    
    for i in range(1,n):
        
        if array[i] != array[i-1]:
            
            array[window] = array[i]
            window += 1
            
    return array[:window]

arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))