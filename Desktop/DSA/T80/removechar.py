# Problem statement
# For a given string(str) and a character X, write a function to remove all the occurrences of X from the given string and return it.

# The input string will remain unchanged if the given character(X) doesn't exist in the input string.

def remove_duplicates(string:str,c:str)->str:
    
    result=""
    
    for char in string:
        
        if char != c:
            
            result += char
            
    return result

input_string = "hello world"
character_to_remove = 'o'
print(remove_duplicates(input_string, character_to_remove))