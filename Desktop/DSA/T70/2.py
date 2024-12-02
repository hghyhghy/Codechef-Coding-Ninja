# Problem statement
# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.

# Note :
# Duplicate number is always present in the given array/list.

def duplicate(array:list)->int:
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            return num
        
        else:
            
            freq[num] =1
            
            
    return -1

a=[1,1,5,6,3,3,0]
print(duplicate(a))