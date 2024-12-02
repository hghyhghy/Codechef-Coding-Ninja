
#peak element 

def main(array):
    
    n=len(array)
    if n==0:
        
        return 0
    
    if n==1:
        
        return array[0]
    
    if array[0]>array[1]:
        
        return array[0]
    
    if array[n-1]>array[n-2]:
        
        return array[n-1]
    
    for i in range(1,n-1):
        
        if array[i-1]<array[i]>array[i+1]:
            
            return i
        
    return -1

a=list(map(int,input().split()))
print(main(a))