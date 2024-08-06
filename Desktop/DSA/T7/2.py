# Count Maximum Consecutive One's in the array

def max_consecutive_one_count(array):
    
    max_count = 0
    current_count = 0
    
    for num in array:
        
        if num  == 1:
            
            current_count += 1
            
        else:
            
            max_count = max(max_count,current_count)
            current_count = 0
            
            
    max_count = max(max_count,current_count)

    return max_count

arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(max_consecutive_one_count(arr))
