# max consecutive ones in the single array 

def max_consecutive_ones(array):
    
    max_count= 0
    current_count= 0
    
    for num in array:
        
        if num ==  1:
            
            current_count += 1
            
        else:
            
            if current_count > max_count:
                
                max_count = current_count
                
            current_count = 0
            
    if current_count > max_count:
        
        max_count = current_count
        
    return max_count

nums = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(nums))