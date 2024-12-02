# Problem statement
# You are given an array 'ARR' of integers. Your task is to modify the array so that all the array elements having zero values get pushed to the left and all the array elements having non-zero value come after them while maintaining their relative order.

# For example :
# Consider the array { 1, 1, 0, 2, 0 }. 
# For the given array the modified array should be {0,0,1,1,2} . 
# Arrays { 0, 0, 1, 2, 1 } and  { 0, 0, 2, 1, 1 } are not the correctly reorganized array even if they have all the zero values pushed to the left as in both the arrays the relative order of non-zero elements is not maintained.

def zer_to_left(array:list[int])->list[int]:
    
    n=len(array)
    zero = n-1
    
    for i in range(n-1,-1,-1):
        
        if array[i] != 0:
            
            array[zero] = array[i]
            zero -=1
            
            
    while zero >=0:
        
        array[zero] =  0
        zero -=1
        
        
    return array

arr = [1, 1, 0, 2, 0]
print(zer_to_left(arr))