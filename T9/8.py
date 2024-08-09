# Search Element in a Rotated Sorted Array


def search_in_rotated_sorted_array(array,target):
    
   
    n=len(array)
    for i in range(n):
        
        if array[i] == target:
            
            return i
            
    return -1


arr = [4,5,6,7,0,1,2,3]
k = 0
print(search_in_rotated_sorted_array(arr,k))