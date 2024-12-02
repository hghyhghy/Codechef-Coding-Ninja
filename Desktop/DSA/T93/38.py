
#house robber
def main(array):
    
    n=len(array)
    if  n==0:
        
        return 0
    
    if n==1:
        
        return array[0]
    
    if n==2:
        
        return max(array[0],array[1])

    
    def max_looting(start,end):
        
        current =0
        
        for i in range(start,end):
            
            main=array[i]
            
            for j in range(i+2,end):
                
                main += array[j]
                
            current =max(current,main)

        
        return current
    
    s1=max_looting(0,n-1)
    s2=max_looting(1,n)
    
    return max(s1,s2)

a=list(map(int,input().split()))
print(main(a))