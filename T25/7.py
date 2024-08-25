# Remove all duplicates from the input string.

def remove_duplicates(string):
    
    result =""

    for char in string:
        
        if char not in result:
            
            result += char
            
    return result

print(remove_duplicates("programming"))