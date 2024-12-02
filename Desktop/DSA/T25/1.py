# Remove characters from a string except alphabets

def removal_of_the_alphabet(string):
    
    alphabets='123456789'

    revised_string=""

    for char in string:
        
        if char in alphabets:
            
            break
        
        else:
            
            revised_string += char
            
            
    return revised_string

print(removal_of_the_alphabet("Hello, World! 123"))