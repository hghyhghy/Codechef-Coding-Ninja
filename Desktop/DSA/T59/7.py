# You are given a string ‘S’ of length ‘N’.

# You must return the longest palindromic substring in ‘S’.

# Note: Return any of them in case of multiple substrings with the same length.

# Example:

# Input: ‘S’ =’badam’

def is_palin(string):
    
    return string == string[::-1]

def main_check(string):
    
    n=len(string)
    max_len=float("-inf")
    
    for start in range(n):
        
        for end in range(start,n):
            
            substring = string[start:end+1]
            
            if is_palin(substring):
                
                length =end-start+1
                
                if length>max_len:
                    
                    max_len=length
                    string1=substring
                    
    return string1

a="badam"
print(main_check(a))