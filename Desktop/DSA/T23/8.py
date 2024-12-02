# Find all repeating elements in an array

def find_all_repeating_elements(array):
    
    freqency={}

    for num in array:
        
        if num in freqency:
            
            freqency[num] += 1
            
        else:
            
            freqency[num] = 1
            
    repeated_elements=[num for num,count in freqency.items() if count > 1]

    return repeated_elements

array = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]
print(find_all_repeating_elements(array))