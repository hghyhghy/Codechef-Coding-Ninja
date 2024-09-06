# Problem statement
# You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.



# Find the total number of occurrences of 'x' in the array/list.



# Example:
# Input: 'n' = 7, 'x' = 3
# 'arr' = [1, 1, 1, 2, 2, 3, 3]

# Output: 2

# Explanation: Total occurrences of '3' in the array 'arr' is 2.

def counting_number_of_occurance(arr,target):
    
    count={}

    for num in arr:
        
        if  num in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
            
    return count.get(target,0)

arr = [1, 1, 1, 2, 2, 3, 3]
x = 3

print(counting_number_of_occurance(arr,x))