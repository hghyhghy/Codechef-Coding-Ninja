# Remove characters from first string present in the second string

def remove_char_from_chars(s1,s2):
    
    char_set=set(s2)
    
    result= "".join(char for char in s1 if char not in char_set)

    return result

print(remove_char_from_chars("hello world", "ole"))