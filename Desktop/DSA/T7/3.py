# Remove Duplicates in-place from Sorted Array

def removing_duplicates(array):
    
    if not array:
        
        return None
    
    unique_index = 1
    
    for i in range(1,len(array)):
        
        if array[i] != array[i-1]:
            
            array[unique_index] = array[i]

            unique_index += 1
            
    return unique_index
    
arr = [1, 1, 2, 3, 3, 4, 5, 5, 6]
length=removing_duplicates(arr)
print("Array after removing duplicates:", arr[:length])
