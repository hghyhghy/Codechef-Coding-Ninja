# Problem statement
# You are given an array/list 'ARR' of integers of length ‘N’. You are supposed to find all the elements that occur strictly more than floor(N/3) times in the given array/list.
from math import floor

def majority(array:list[int])->int:
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num]+=1 
            
        else:
            
            freq[num] = 1
            
    n=len(array)
    thr=floor(n/3)
    res=[]

    for num,count in freq.items():
        
        if count >thr:
            
            res.append(num)
        
    return  res

arr = [3, 1, 2, 2, 3, 3, 3, 4, 4]
print(majority(arr))
    