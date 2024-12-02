# Problem statement
# For a given string(str), remove all the consecutive duplicate characters.

# Example:
# Input String: "aaaa"
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"

def remove_consecutive_duplicates_character(string):
    
    if not string:
        
        return None
    stack=""
    prev_char=None
    
    for char  in string:
        
        if char != prev_char:
            stack += char
            prev_char=  char
            
    return "".join(stack)

input_str = "aabbbcc"
print(remove_consecutive_duplicates_character(input_str))