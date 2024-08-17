# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

def first_missing_positive(number):
    
    num_set= set()

    for num in number:
        
        if num > 0:
            
            num_set.add(num)

    positive = 1
    
    while positive in num_set:
        
        positive += 1
        
    return positive

nums = [3, 4, -1, 1]
print(first_missing_positive(nums))