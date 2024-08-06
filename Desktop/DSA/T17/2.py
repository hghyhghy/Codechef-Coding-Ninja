# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def majority_element_three(array):
    
    freq={}
    
    for num in array:
        
        if num in  freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    n=len(array)
    threshold = n//3

    
    result= [num for num,count in freq.items() if count > threshold]
    
    return result

nums = [3, 2, 3]
print(majority_element_three(nums))