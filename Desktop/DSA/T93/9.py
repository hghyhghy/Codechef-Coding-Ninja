#next greater element in the circular array 

def main(array:list[int])->list[int]:
    
    n=len(array)
    result=[-1]*n
    
    for i in range(n):
        
        for j in range(1,n):
            
            next_greater=(i+j)%n
            
            if array[next_greater]>array[i]:
                
                result[i]=array[next_greater]
                break
            
    return result

arr = [1, 5, 3, 4, 2]
print(main(arr))