

#majority element 

def main(array):
    
    freq={}
    n=len(array)

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
            
    half=n//2
    
    for num,count in freq.items():
        
        if count > half:
            
            return num
        
    
    return -1

nums=list(map(int,input().split()))
print(main(nums))