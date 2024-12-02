# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

def returning_duplicate(array):
    
    count= {}

    for num in array:
        
        if num in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
            
    duplicates=sorted([num for num,freq in count.items() if freq == 2])

    return duplicates

nums = [4, 3, 2, 7, 8, 2, 1, 4]
print(returning_duplicate(nums))