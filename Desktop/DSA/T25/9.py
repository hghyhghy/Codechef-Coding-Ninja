# Print all the duplicates in the input string.

def print_all_duplicates(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
            
    result="".join(x for x,count in freq.items() if count > 1)
    
    return result

print(print_all_duplicates("programming"))

