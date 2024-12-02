
#first negative in every k sized window 

def main(array:list[int],k:int)->list[int]:
    
    n=len(array)
    result=[]
    
    for start in range(n-k+1):
        
        negative= 0
        
        for end in range(start,start+k):
            
            if array[end]<negative:
                
                negative =  array[end]
                break
        
        result.append(negative)

    
    return result

arr = [5, -3, 2, 3, -4]
k = 2
print(main(arr,k))

