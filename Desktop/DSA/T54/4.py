# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

def longest_substring_without_repeating_char(string):
    
    n=len(string)
    max_length= float("-inf")

    for start in range(n):
        
        seen=set()
        current =0
        
        for end in range(start,n):
            
            if string[end] in seen:
                
                break
            
            seen.add(string[end])
            current += 1
            
        max_length =max(max_length,current)

    return max_length

s = "abcabcbb"
print(longest_substring_without_repeating_char(s))
                
                