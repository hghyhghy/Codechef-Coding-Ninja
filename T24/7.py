# Remove all vowels from the string

def removal_of_vowels(string):
    
    vowels='aeiouAEIOU'

    revised_char=""

    for char in string:
        
        if char not in vowels:
            
            revised_char += char
            
    
    return revised_char

print(removal_of_vowels("hello")) 