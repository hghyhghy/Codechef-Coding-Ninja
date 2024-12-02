# Find all non-repeating elements in an array

def non_repeating_character(array):
    
    count={}

    for num in array:
        
        if num  in count:
            
            count[num] += 1
            
        else:
            count[num]  = 1
            
    non_repeated = [item for item,freq in  count.items() if freq == 1]
    
    return non_repeated

array = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]
print(non_repeating_character(array))