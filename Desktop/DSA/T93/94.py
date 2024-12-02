

#top k frequent element 
def main(array,k):
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] =1

    new= sorted(freq.items(),key=lambda x:x[1],reverse=True)

    return [list[0] for list in new[:k]]

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))
