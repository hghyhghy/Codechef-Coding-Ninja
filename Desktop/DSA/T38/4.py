# You are given a string 'S' of length 'N' consisting of lowercase English alphabet letters. You are also given a positive integer 'K'.

# Now, a substring of this string is good if it contains at most 'K' distinct characters. A string 'X' is a substring of string 'Y' if it can be obtained by deletion of several continuous elements(possibly zero) from the beginning and the end from the string 'Y'.

# Your task is to return the maximum size of any good substring of the string 'S'.

# Example:
# ‘S’ = “bacda” and ‘K’ = 3.

def subarray_with_distinct_characters(string):
    
    n=len(string)
    max_len=0
    
    for i in range(n):
        
        seen=set()

        for j in range(i,n):
            
            if string[j] in seen:
                
                break
            
            seen.add(string[j])

            max_len = max(max_len,j-i+1)
            
    return max_len

s = "abcabcbb"
print(subarray_with_distinct_characters(s))