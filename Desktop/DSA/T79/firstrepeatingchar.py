# Ninja is now bored with numbers and is now playing with characters but hates when he gets repeated characters. Ninja is provided a string, and he wants to return the first unique character in the string.The string will contain characters only from the English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z'). If there is no non-repeating character, print the first character of the string. If there is no non-repeating character, return the first character of the string.

def first_repeating_char(string:str)->str:
    
    freq={}
    
    for char in string:
        
        if char in freq:
            
            freq[char] += 1

        else:
            
            freq[char] = 1
            
    for char in string:
        
        if freq[char] == 1:
            
            return char
        
    
    return string[0]

s = "swiss"

print(first_repeating_char(s))