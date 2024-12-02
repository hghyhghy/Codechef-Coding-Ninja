# 229. Majority Element II
# Medium
# Topics
# Companies
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def majority_element(array):
    
    freq={}
    for num in array:
        
        if  num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    n=len(array)
    limit=n//3
    result=[]

    for num,count in freq.items():
        
        if count >limit:
            
            result.append(num)

    return result

nums = [3, 2, 3]
print(majority_element(nums))