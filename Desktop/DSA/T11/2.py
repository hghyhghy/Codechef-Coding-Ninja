# Find minimum in Rotated Sorted Array

def find_minimum_in_rotated_sorted_array(array):
    
    if not array:
        
        return None
    
    minimum=array[0]

    
    for num in array:
        
        if num < minimum:
            
            minimum=num
            
    return minimum

rotated_sorted_array = [4, 5, 6, 7, 0, 1, 2]
print(find_minimum_in_rotated_sorted_array(rotated_sorted_array))