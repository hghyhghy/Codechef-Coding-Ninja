# Problem statement
# Given a string input of length n, find the length of the longest substring without repeating characters i.e return a substring that does not have any repeating characters.

# Substring is the continuous sub-part of the string formed by removing zero or more characters from both ends.

def longest_substring_without_repeat_char(array):
    
    n=len(array)
    max_lenght= 0
    longest=""    
    for start in range(n):
        
        seen=set()
        substring =""
        for end in range(start,n):
            
            if array[end]in seen:
                
                break
            
            seen.add(array[end])
            substring += array[end]
            
            length =end-start+1
            if length > max_lenght:
                
                max_lenght =length
                longest =substring
            
            
    return max_lenght,longest if max_lenght else None

s = "abcabcbb"
print(longest_substring_without_repeat_char(s))