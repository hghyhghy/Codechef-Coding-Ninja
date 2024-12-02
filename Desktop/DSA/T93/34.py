#repeat and missing 
def main(array):
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] =1
            
    
    repeat=-1
    missing=-1
    n=len(array)
    
    
    for i in range(1,n+1):
        
        if i not in freq:
            
            missing =i
            
        elif freq[i] == 2:
            
            repeat = i
            
    return repeat,missing

arr=list(map(int,input().split()))
print(main(arr))