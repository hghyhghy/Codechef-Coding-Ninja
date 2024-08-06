# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def first_non_repeating_character(string):
    
    count={}

    for char in string:
        
        if char in count:
            
            count[char] += 1
            
        else:
            
            count[char] = 1
            
            
    for index,char in enumerate(string):
        
        if count[char] == 1:
            
            return index
        
    
    return -1

s = "loveleetcode"
print(first_non_repeating_character(s))