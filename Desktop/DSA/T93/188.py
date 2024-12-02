
#sorted binary string



def main(array):
    
    n=len(array)
    current=0
    
    for i in range(n):
        
        if array[i] == 0:
            
            array[i],array[current] = array[current],array[i]
            
            current +=1
            
    return array

arr = [1, 0, 1, 0, 1, 0, 1, 0]
print(main(arr))