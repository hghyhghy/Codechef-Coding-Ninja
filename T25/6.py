# Return maximum occurring character in the input string

def max_occuring_character(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
            
    max_char=None
    max_count = 0
    
    for char,count in freq.items():
        
        if count > max_count:
            
            max_count = count
            max_char = char
            
            
    return max_char,max_count

print(max_occuring_character("hello")) 