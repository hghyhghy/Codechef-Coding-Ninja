# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

def finding_duplicate(array):
    
    freq={}
    for num in array:
        
        if num in freq:
            
            freq[num] +=1
            
        else:
            
            freq[num] = 1
            
    reuslt=[num for num,count in freq.items() if count > 1]

    return reuslt


nums = [4,3,2,7,8,2,3,1]
print(finding_duplicate(nums))