
#top k frequent elements

def main(array,k):
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] +=1 
            
        else:
            
            freq[num] = 1
            
    new=sorted(freq,key=lambda x: freq[x],reverse=True)
    
    return new[:k]

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))

