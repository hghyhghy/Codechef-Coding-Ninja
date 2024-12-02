# Given an array 'ARR' of integers of size N in which two elements appear exactly once and all other elements appear exactly twice. Your task is to find the two elements that appear only once.

# Note
#  1. Input will always have only two integers that appear exactly once rest will appear twice.
#  2. Try to do this in linear time and constant space.

def single_number(array:list[int])->list[int]:
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] =  1
            
    result=[]
    
    for num,count in freq.items():
        
        if count ==1:
            
            result.append(num)

    
    return result

arr = [2, 3, 7, 9, 11, 2, 3, 11]
print(single_number(arr))