# Find Non-repeating characters of a String

def non_repeating_character(string):
    
    non_repeating_chars=""
    frequency={}

    for char in string:
        
        if char in frequency:
            
            frequency[char] += 1
            
        else:
            
            frequency[char] = 1
            
    for val,count in frequency.items():
        
        if  count == 1:
            
            non_repeating_chars += val
            
    return non_repeating_chars


a="google"
print(non_repeating_character(a))