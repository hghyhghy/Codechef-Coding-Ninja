# Given a string input of length n, find the length of the longest substring without repeating characters i.e return a substring that does not have any repeating characters.

# Substring is the continuous sub-part of the string formed by removing zero or more characters from both ends. using set and two for loop  

def longest_substring_without_repeating_char(string:str)->int:
    
    n=len(string)
    max_length= float("-inf")
    
    for start in range(n):
        
        seen=set()
        
        for end in range(start,n):
            
            if string[end] in seen:
                
                break
            seen.add(string[end])

            max_length =max(max_length,end-start+1)
            
    return max_length

a="abcabcbb"
print(longest_substring_without_repeating_char(a))