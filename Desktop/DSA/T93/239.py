

#move all zero to end 

def main(array):
    
    n=len(array)
    j=0
    
    for i in range(n):
        
        if array[i] == 0:
            
            array[j],array[i] =  array[i],array[j]

            j +=1
            
    return array

a=[0, 1, -2, 3, 4, 0, 5, -27, 9, 0]
print(main(a))