# Problem statement
# Given a string 'S' of length 'L', return the length of the longest substring without repeating characters.

# Example:

# Suppose given input is "abacb", then the length of the longest substring without repeating characters will be 3 ("acb").

def longest_substring_without_repeating(string:str)->int:
    
    n=len(string)
    longest = 0
    
    for start in range(n):
        
        seen=set()
        
        for end in range(start,n):
            
            if string[end] in seen:
                
                break
            
            seen.add(string[end])
            
            longest=max(longest,end-start+1)
            
    return longest

S = "abacb"
print(longest_substring_without_repeating(S))