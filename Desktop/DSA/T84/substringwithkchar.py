# Problem statement
# You are given a string 'S' of length 'N' consisting of lowercase English alphabet letters. You are also given a positive integer 'K'.

# Now, a substring of this string is good if it contains at most 'K' distinct characters. A string 'X' is a substring of string 'Y' if it can be obtained by deletion of several continuous elements(possibly zero) from the beginning and the end from the string 'Y'.

# Your task is to return the maximum size of any good substring of the string 'S'.

# Example:
# ‘S’ = “bacda” and ‘K’ = 3.

# So, the substrings having at most ‘3’ distinct characters are called good substrings. Some possible good substrings are:
# 1. “bac”
# 2. “acd”
# 3. “acda”

# The substring “acda” is the largest possible good substring, as we cannot get any other substring of length 5 or more having distinct characters less than or equal to ‘3’. Thus, you should return ‘4’ as the answer.

def substring_with_k_char(string:str,k:int)->int:
    
    n=len(string)
    max_len=float("-inf")
    
    for i in range(n):
        
        seen=set()
        
        for j in range(i,n):
            
            seen.add(string[j])

            if len(seen)> k:
                
                break
            
            max_len=max(max_len,j-i+1)
            
    return max_len

S = "bacda"
K = 3
print(substring_with_k_char(S,K))
