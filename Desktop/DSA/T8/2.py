# max consecutive ones 

def max_consecutive(array):
    
    count = 0
    max_count = 0
    
    for num in array:
        
        if num == 1:
            
            count += 1
            
        else:
            max_count = max(max_count,count)
            
            count = 0
        
    return max_count

nums = [1, 1, 0, 1, 1, 1, 0, 1]
print(max_consecutive(nums))