# You are given a string (STR) of length N, consisting of only the lower case English alphabet.

# Your task is to remove all the duplicate occurrences of characters in the string.

def remove_duplicates_from_string(string:str) ->str:
    
    if not string or len(string) == 1:
        
        return  string
    
    result=""
    seen=set()

    for char in string:
        
        if char in seen:
            
            continue
        
        seen.add(char)
        result += char
        
    
    return result

a="abracadabra"
print(remove_duplicates_from_string(a))