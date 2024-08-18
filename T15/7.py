# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

def single_number(array):
    
    count={}

    for num in array:
        
        if num in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
            
            
    for val,cnt in count.items():
        
        if cnt  == 1:
            
            return val
        
    return 0

nums = [2, 2, 1, 3, 3]
print(single_number(nums))