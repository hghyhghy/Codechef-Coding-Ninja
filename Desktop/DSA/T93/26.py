#sngle number 

def main(arr:list[int])->int:
    
    freq={}
    
    for num in arr:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    r=[]
    for num,count in freq.items():
        
        if count  == 1:
            
            r.append(num)
            
    return r

a=list(map(int,input().split()))
print(main(a))
    