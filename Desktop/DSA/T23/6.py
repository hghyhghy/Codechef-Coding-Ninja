# Average of all elements in an array

def fid_average_of_all_elements(arr):
    
    total = 0
    count = 0
    
    for num in arr:
        
        total += num
        count += 1
        
        
    if count == 0:
        
        return 0 
    
    
    return total / count

array = [10, 20, 30, 40, 50]
print(fid_average_of_all_elements(array))