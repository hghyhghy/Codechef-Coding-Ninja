# Problem statement
# You are given an array ‘ARR’ consisting of ‘N’ strings. Your task is to find the longest common prefix among all these strings. If there is no common prefix, you have to return an empty string.

# A prefix of a string can be defined as a substring obtained after removing some or all characters from the end of the string.

# For Example:
# Consider ARR = [“coding”, ”codezen”, ”codingninja”, ”coders”]
# The longest common prefix among all the given strings is “cod” as it is present as a prefix in all strings. Hence, the answer is “cod”.

def longest_common_prefix(strings):
    
    if not strings:
        
        return None
    
    prefix=  strings[0]

    for string in strings:
        
        while not string.startswith(prefix):
            
            prefix=prefix[:-1]

            if not prefix:
                
                return  " "
            
            
    return prefix
ARR = ["flower", "flow", "flight"]
print(longest_common_prefix(ARR))