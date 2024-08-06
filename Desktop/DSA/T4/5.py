# Remove all vowels from the string

def removing_all_vowels(string):
    
    vowels={'a','e','i','o','u'}
    temp = ""

    for char in string:
        
        if char not in vowels:
            
            temp += char
            
    return temp


a="take u forward"
print(removing_all_vowels(a))