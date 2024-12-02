

#moving negative to  front  

def main(array):
    
    n=len(array)
    j = 0
    
    
    for  i in range(n):
        
        if array[i] < 0:
            
            array[j] ,array[i] = array[i],array[j]

            j +=1
            
    return array

s=[1, 2, -3, 4, -4, -5]
print(main(s))