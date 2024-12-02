
#sort array by freq

def main(array):
    
    freq={}
    first={}
    
    for index,num in enumerate(array):
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num]=1
            first[num] = index
            
    new_array =  sorted(array,key=lambda x : (-freq[x],first[x]))
    
    return new_array

n=list(map(int,input().split()))
print(main(n))