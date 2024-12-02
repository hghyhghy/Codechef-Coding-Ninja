# removal _of spaces from the string

def removal_of_string(string):
    
    result=""

    for char in string:
        
        if char !=  " ":
            
            result += char
            
    
    return result

print(removal_of_string("hello  world"))