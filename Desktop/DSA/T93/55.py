

#majority element 

def main(arr,k):
    
    freq={}
    
    for  num in arr:
        
        if num in freq:
            
            freq[num] +=1
            
        else:
            
            freq[num] =1
            
    
    n=len(arr)
    limit=n//k
    r=[]

    for num,count in freq.items():
        
        if count >= limit:
            
            r.append(num)

    return r

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))