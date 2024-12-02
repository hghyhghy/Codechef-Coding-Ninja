# Problem statement
# You are given a sorted array 'ARR' and a number 'X'. Your task is to count the number of occurrences of 'X' in 'ARR'.

# Note :
# 1. If 'X' is not found in the array, return 0.
# 2. The given array is sorted in non-decreasing order.

def occurance_of_a_number(array:list[int],x:int)->int:
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    if x in freq:
        
        return freq.get(x,0)
    
    else:
        
        return 0
    
a=[2,1,3,5,6,0,9,0]
print(occurance_of_a_number(a,0))