# Count frequency of each element in an array using dictionary

def count_frequency_using_dictionary(array):
    
    frequency={}

    for num in array:
        
        if num in frequency:
            
            frequency[num] += 1
            
        else:
            
            frequency[num] = 1
            
            
    return frequency

