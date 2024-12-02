# Problem statement
# You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.

# Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.

# Your task is to find the missing number (M) and the repeating number (R).

# For example:
# Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
# The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R). 

def missing_and_repeatative(array:list[int])->list[int]:
    
    freq={}
    n=len(array)
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    repeat=-1
    missing=-1
    
    for num in range(1,n+1):
        
        if  num in freq:
            
            if freq[num] == 2:
                
                repeat =num
                
        else:
                
            missing = num
                
    return [repeat,missing]

arr = [6, 4, 3, 5, 5, 1]
print(missing_and_repeatative(arr))
    