
#sort array elements by frequency 

def main(array:list[int])->list[int]:
    
    freq={}
    first={}
    
    
    for  index,num in enumerate(array):
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num]=1
            first[num] = index 
            
    
    result=sorted(array,key=lambda x:(-freq[x],first[x]))
    return  result

arr=list(map(int,input().split()))
print(main(arr))