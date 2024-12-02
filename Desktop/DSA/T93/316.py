

#moving zeroes to the end 

def main(array):
    
    unique=0
    n=len(array)

    for i in range(n):
        
        if array[i] != 0:
            
            array[unique] = array[i]
            
            unique +=1

        
    for i in range(unique,n):
        
        array[i] =0
        
    
    return array

nums = [0,1,0,3,12]
print(main(nums))

