
# Contributed by
# 188 upvotes
# Asked in companies
# Problem statement
# You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.



# Find the total number of occurrences of 'x' in the array/list.



# Example:
# Input: 'n' = 7, 'x' = 3
# 'arr' = [1, 1, 1, 2, 2, 3, 3]

# Output: 2

# Explanation: Total occurrences of '3' in the array 'arr' is 2.

def occurance_of_th_number(array:list[int],target:int)->int:
    
    freq={}
    
    for num in array:
        
        if  num in freq:
            
            freq[num]+=1
        
        else:
            
            freq[num] = 1
            
    
    return freq.get(target,0)

arr = [1, 1, 2, 2, 2, 3, 3, 4]
x = 2
print(occurance_of_th_number(arr,x))