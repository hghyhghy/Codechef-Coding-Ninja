# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majority_element_from_the_array(arry):
    
    count={}
    n=len(arry)

    for num in arry:
        
        if num in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
            
    for val,cnt in count.items():
        
        if cnt > n//2:
            
            return val
    
    return 0

nums = [2,2,1,1,1,2,2]
print(majority_element_from_the_array(nums))