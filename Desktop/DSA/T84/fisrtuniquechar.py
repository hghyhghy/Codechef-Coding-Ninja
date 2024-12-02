# Given a string ‘STR’ consisting of lower case English letters, the task is to find the first non-repeating character in the string and return it. If it doesn’t exist, return ‘#’.

# For example:

# For the input string 'abcab', the first non-repeating character is ‘c’. As depicted the character ‘a’ repeats at index 3 and character ‘b’ repeats at index 4. Hence we return the character ‘c’ present at index 2.

def first_unique_element(string:str)->str:
    
    freq={}
    
    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] =1
            
    for char in string:
        
        if freq[char] == 1:
            
            return char
        
    
    return -1

s="abcab"
print(first_unique_element(s))