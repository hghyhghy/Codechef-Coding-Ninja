

#single element

def main(array):
    
    freq={}
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    
    for num,count in freq.items():
        
        if count == 1:
            
            return num
        
    
    return -1

a=list(map(int,input().split()))
print(main(a))