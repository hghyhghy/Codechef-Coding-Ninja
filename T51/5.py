# Problem statement
# For a given string(str), remove all the consecutive duplicate characters.

# Example:
# Input String: "aaaa"
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"
#  Input Format:
# The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.
# Output Format:
# The only line of output prints the updated string.

def remove_consecutive_suplicates(array):
    
    n=len(array)
    if not array or n==1:
        
        return 
    
    result=""

    for i in range(n):
        
        if array[i] != array[i-1]:
            
            result += array[i]

    
    return result

a="aabbbcc"
print(remove_consecutive_suplicates(a))

