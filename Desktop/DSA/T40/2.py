# Problem statement
# Given a string 'S' of length 'L', return the length of the longest substring without repeating characters.

# Example:

# Suppose given input is "abacb", then the length of the longest substring without repeating characters will be 3 ("acb").

def longest_substring_without_repeating_chars(string):
    
    n=len(string)
    max_lenght = 0
    
    for start in range(n):
        
        seen=set()

        for end in range(start,n):
            
            if string[end] in seen:
                
                break
            
            seen.add(string[end])

            length=end-start+1
            
            max_lenght=max(max_lenght,length)

    return max_lenght

s = "abcabcbb"

print(longest_substring_without_repeating_chars(s))
