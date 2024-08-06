# Remove characters from a string except alphabets

def remove_all_alphabets(string):
    
    result=""

    for char in string:
        
        if char.isalpha():
            
            result += char
    
    return  result

a = "Hello, World! 123"
print(remove_all_alphabets(a))