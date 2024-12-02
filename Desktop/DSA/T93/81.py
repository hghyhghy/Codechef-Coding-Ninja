
#majority element 

def main(array):
    
    n=len(array)
    limit=n//2
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num]+=1
            
        else:
            
            freq[num] = 1
            
    
    for num,count in freq.items():
        
        if count  > limit:
            
            return num
        
    return -1

num=list(map(int,input().split()))
print(main(num))