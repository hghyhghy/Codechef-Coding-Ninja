# Problem statement
# You are given a string ‘S’ of length ‘N’. You have to return all the characters in the string that are duplicated and their frequency.

def duplicate_character_in_string(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
            
    for char,count in freq.items():
        
        if count > 1:
            
            return count,char
    
    return None

a="apple"
print(duplicate_character_in_string(a))