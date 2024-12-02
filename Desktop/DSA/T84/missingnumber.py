# Problem statement
# Given an array ‘a’ of size ‘n’-1 with elements of range 1 to ‘n’. The array does not contain any duplicates. Your task is to find the missing number.



# For example:
# Input:
# 'a' = [1, 2, 4, 5], 'n' = 5

# Output :
# 3

# Explanation: 3 is the missing value in the range 1 to 5.

def missing_number_using_freq(array:list[int])->int:
    
    freq={}
    
    for num in array:
        
        freq[num] = True
        
    for i in range(1,len(array)+1):
        
        if  i not in freq:
            
            return i
        
        
    return -1

a=[1,2,4,5]
print(missing_number_using_freq(a))