# Find Non-repeating characters of a String

def non_repeating_chars(strings):
    
    freq={}

    for char in strings:
        
        if char in freq:
            
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
            
    

    new_srtring="".join(char for char,count in freq.items() if count == 1)
    
    return new_srtring

string = "swiss"
print(non_repeating_chars(string))