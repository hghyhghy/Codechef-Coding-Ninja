
#three sum

def main(array,target):
    
    n=len(array)
    seen=set()
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            for  k in range(j+1,n):
                
                if array[i]+array[j]+array[k] == target:
                    
                    result= tuple(sorted(array[i],array[j],array[k]))

                    seen.add(result)


    if result:
        
        return [list(t) for t in result]
    
    else:
        
        return -1
    
