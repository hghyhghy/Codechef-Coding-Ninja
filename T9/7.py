# Find minimum in Rotated Sorted Array

def minimum_rotated_sorted_array(array):
    
    minimum=array[0]
    n=len(array)

    for i in range(n):
        
        if array[i] < minimum:
            
            minimum =  array[i]

    return  minimum

arr = [4,5,6,7,0,1,2,3]
print(minimum_rotated_sorted_array(arr))
