# Calculate sum of the elements of the array

def sum_of_elements_of_array(arr):
    
    total = 0 
    
    for num in arr:
        
        total += num
        
    return total
totalnums = [1, 2, 3, 4, 5]
print(sum_of_elements_of_array(totalnums))
