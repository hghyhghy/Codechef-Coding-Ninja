# Problem statement
# You have been given a string 'STR' of words. You need to replace all the spaces between words with “@40”.

def remove_suplicates_with_letters(string):
    
    if not string:
        
        return None
    result=""

    for char in string:
        
        if char == " ":
            
            result += "@40"

        else:
            
            result += char
            
    return result

str_input = "This is a test string"
print(remove_suplicates_with_letters(str_input))