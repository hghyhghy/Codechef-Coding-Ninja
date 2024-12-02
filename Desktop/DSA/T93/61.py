
#longest subarray with zero sum 

def main(array:list[int])->int:
    
    n=len(array)
    max_len =float("-inf")
    
    
    for i in range(n):
        
        current = 0
        
        for j in range(i,n):
            
            current += array[j]
            
            if current == 0:
                
                max_len = max(max_len,j-i+1)
                
    return max_len

array=list(map(int,input().split()))
print(main(array))
