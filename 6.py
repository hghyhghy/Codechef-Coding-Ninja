# move zeroes to the end 

def move_all_zeroes_to_end(array):
    
    left_zeroes = 0 
    n=len(array)

    for current in range(n):
        
        if array[current] != 0:
            
            array[left_zeroes],array[current] = array[current],array[left_zeroes]
            left_zeroes += 1
            
            
    return array

arr = [0, 1, 0, 3, 12]
print(move_all_zeroes_to_end(arr))