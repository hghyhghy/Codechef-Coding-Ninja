

#majority element

def main(array):
    
    n=len(array)
    limit=n//3
    r=[]
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    
    for num,count in freq.items():
        
        if count > limit:
            
            r.append(num)

    
    return r

num=list(map(int,input().split()))
print(main(num))