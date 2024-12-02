# Problem statement
# You are given a string ‘str’ of size ‘N’. Your task is to remove consecutive duplicates from this string recursively.

# For example:

# If the input string is ‘str’ = ”aazbbby”, then your output will be “azby”.
# Note that we are just removing adjacent duplicates.

def remove_consecutive_duplicates(string):
    
    if not string:
        
        return ""

    n=len(string)
    dp=""

    for i in range(n):
        
        if string[i] != string[i-1]:
            
            dp += string[i]

    return dp

s = "aabbccddeeff"
print(remove_consecutive_duplicates(s))