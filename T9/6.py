# Contains Duplicate : Check if a value appears atleast twice

def contains_duplicate(array):
    
    frequency={}

    for num in array:
        
        if num in frequency:
            
            frequency[num] += 1
            
        else:
            
            frequency[num] = 1
            
    for count in frequency.values():
        
        if count > 1:
            
            return "True"
            

nums = [1, 2, 3, 1]
print(contains_duplicate(nums))