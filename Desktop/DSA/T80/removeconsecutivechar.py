# Problem statement
# For a given string(str), remove all the consecutive duplicate characters.

# Example:
# Input String: "aaaa"
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"
#  Input Format:
# The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.

def remove_duplicates_consecutive(sting:str)->str:
    
    if not sting:
        
        return None
    
    result = sting[0]
    
    n=len(sting)
    
    for  i in range(n):
        
        if sting[i] != sting[i-1]:
            
            result += sting[i]
            
    
    return result

input_string1 = "aaaa"
print(remove_duplicates_consecutive(input_string1))