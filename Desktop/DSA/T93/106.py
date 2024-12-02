

#find duplicate

def main(arr):
    
    freq={}
    
    for num in arr:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] =1 
            
    num=[num for num,count in freq.items() if count  == 1]
    
    return num

arr=list(map(int,input().split()))
print(main(arr))
