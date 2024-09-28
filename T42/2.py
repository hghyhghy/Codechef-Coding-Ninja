# Problem statement
# You are given a sorted integer array 'arr' of size 'n'.



# You need to remove the duplicates from the array such that each element appears only once.



# Return the length of this new array.



# Note:
# Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory. 

def remove_duplicates_from_array(array):
    
    if array is None:
        
        return None
    
    n=len(array)
    i=0
    
    for j in range(1,n):
        
        if array[j] != array[i]:
            
            i += 1
            array[i]= array[j]
            
            
    return array[:i+1]

arr = [1, 1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates_from_array(arr))

