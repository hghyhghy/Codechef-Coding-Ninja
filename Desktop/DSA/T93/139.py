

#longest substring without repeat char

def main(string):
    
    n=len(string)
    max_length=float("-inf")
    
    for i in range(n):
        
        seen=set()
        curr=0
        
        for  j in range(i,n):
            
            if string[j] in seen:
                
                break
            
            seen.add(string[j])
            curr +=1
            
        
        max_length = max(max_length,curr)

    
    return max_length

