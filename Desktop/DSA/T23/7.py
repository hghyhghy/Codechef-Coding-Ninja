# Remove duplicates from a sorted array

def remove_duplicate_from_the_array(array):
    
    if not array:
        
        return None
    
    i=0
    
    for j in range(1,len(array)):
        
        if array[j] != array[i]:
            
            i += 1
            
            array[i] = array[j]

    return array[:i+1]

sorted_array = [1, 1, 2, 3, 3, 4, 5, 5]
print(remove_duplicate_from_the_array(sorted_array))