#selection sort 

def  main(array:list[int])->list[int]:

    n=len(array)

    
    for i in range(n):
        
        minimum=i
        
        for j in range(i+1,n):
            
            if  array[j]< array[minimum]:
                
                minimum = j
                
        
        array[i],array[minimum]=array[minimum],array[i]
        
    
    return array
arr = [64, 25, 12, 22, 11]
print(main(arr))
    
    