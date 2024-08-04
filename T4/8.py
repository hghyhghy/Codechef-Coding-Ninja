# Remove all duplicates from the input string.

def remove_duplicates(string):
    
    non_duplicate=""
    frequency={}

    for char in string:
        
        if char in frequency:
            
            frequency[char] += 1
            
        else:
            
            frequency[char] = 1
            
            
    non_duplicate="".join(char for char in string if frequency[char] == 1)
            
    return non_duplicate


s="bcabc"
print(remove_duplicates(s))