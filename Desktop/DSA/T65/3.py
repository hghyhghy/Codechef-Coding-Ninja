# Given a string input of length n, find the length of the longest substring without repeating characters i.e return a substring that does not have any repeating characters.

# Substring is the continuous sub-part of the string formed by removing zero or more characters from both ends.

def longest_substring_without_repeating_char(string:str)->int:
    
    n=len(string)
    max_len = float("-inf")

    for start in range(n):
        
        seen=set()

        for end in range(start,n):
            
            if string[end] in seen:
                
                break
            
            seen.add(string[end])

            max_len =max(max_len,end-start+1)
            
    return max_len

a="abcabcbb"
print(longest_substring_without_repeating_char(a))
