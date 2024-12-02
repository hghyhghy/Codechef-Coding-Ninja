#swapalternatives 

def main(array:list[int])->list[int]:
    
    n=len(array)

    for i in range(0,n-1,2):
        
        array[i],array[i+1]=array[i+1],array[i]
        
    
    return array
arr = [1, 2, 3, 4, 5, 6]
print(main(arr))