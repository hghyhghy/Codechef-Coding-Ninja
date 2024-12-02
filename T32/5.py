# Problem statement
# You are given a sorted array 'arr' of positive integers of size 'n'.



# It contains each number exactly twice except for one number, which occurs exactly once.



# Find the number that occurs exactly once.



# Example :
# Input: ‘arr’ = {1, 1, 2, 3, 3, 4, 4}.

# Output: 2

# Explanation: 1, 3, and 4 occur exactly twice. 2 occurs exactly once. Hence the answer is 2.

def finding_the_single_element(array):
    
    freq={}

    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
            
    result= [num for num,count in freq.items() if count == 1]

    return result

a=[ 1, 1, 2, 3, 3, 4, 4]
print(finding_the_single_element(a))