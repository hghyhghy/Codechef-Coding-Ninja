# You are given a string (STR) of length N, consisting of only the lower case English alphabet.

# Your task is to remove all the duplicate occurrences of characters in the string.

# For Example:
# If the given string is:
# abcadeecfb

# Then after deleting all duplicate occurrences, the string looks like this:
# abcdef

def remove_duplicates(string:str)->str:
    
    seen=set()
    result=[]
    
    for c in string:
        
        if c not in seen:
            
            seen.add(c)
            result.append(c)
            
    return "".join(result)

a="abcadeecfb"
print(remove_duplicates(a))