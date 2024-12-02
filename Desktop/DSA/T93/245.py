

#peak element 

def main(array):
    
    n=len(array)
    if n==0:
        
        return -1
    
    if n==1:
        
        return 0
    
    if array[0]> array[1]:
        
        return 0
    
    if array[n-1]>array[n-2]:
        
        return n-1
    
    for i in range(1,n-1):
        
        if array[i]>array[i-1] and array[i]> array[i+1]:
            
            return array[i],i
        
    return -1

arr = [1, 3, 20, 4, 1]
print(main(arr))