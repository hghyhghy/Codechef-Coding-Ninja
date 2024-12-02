# For a given input string(str), find and return the total number of words present in it.

# It is assumed that two words will have only a single space in between. Also, there wouldn't be any leading and trailing spaces in the given input string.

def count_words(strings):
    
    count = 0
    
    for char in strings:
        
        if char  == " ":
            
            count += 1
            
        
            
    count += 1
            
            
    return count

input_string = "Hello world this is OpenAI"
print(count_words(input_string))