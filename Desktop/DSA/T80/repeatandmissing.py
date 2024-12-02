# Problem statement
# You are given an array 'nums' consisting of first N positive integers. But from the N integers, one of the integers occurs twice in the array, and one of the integers is missing. You need to determine the repeating and the missing integer.

# Example:
# Let the array be [1, 2, 3, 4, 4, 5]. In the given array ‘4’ occurs twice and the number ‘6’ is missing.

def repeat_and_missing(array:list[int])->int:
    
    freq={}
    
    for num in array:
        
        if num  in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
            
    repeat= -1
    missing =-1
    n=len(array)
    
    for i in range(1,n+1):
        
        if i not in freq:
            
            missing = i
            
        elif freq[i] == 2:
            
            repeat = i
            
            
    return repeat,missing if repeat and missing else -1

nums = [1, 2, 3, 4, 4, 5]
print(repeat_and_missing(nums))