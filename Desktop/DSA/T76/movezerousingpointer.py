
def move_zero(array):
    
    n=len(array)
    non_zero=0
    
    for i in range(n):
        
        if array[i] != 0:
            
            array[non_zero],array[i] =array[i],array[non_zero]
            
            non_zero +=1 
            
    return array

arr = [0, 1, -2, 3, 4, 0, 5, -27, 9, 0]
print(move_zero(arr))