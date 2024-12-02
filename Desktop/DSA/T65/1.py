# Problem statement
# You are given a string 'str' of length 'N'.



# Your task is to return the longest palindromic substring. If there are multiple strings, return any.



# A substring is a contiguous segment of a string.



# For example :
# str = "ababc"

# The longest palindromic substring of "ababc" is "aba", since "aba" is a palindrome and it is the longest substring of length 3 which is a palindrome. 

# There is another palindromic substring of length 3 is "bab". Since starting index of "aba" is less than "bab", so "aba" is the answer.

def check(string:str) ->bool:
    
    return string == string[::-1]

def main(string:str)->str:
    
    n=len(string)
    max_len= float("-inf")
    
    for start in range(n):
        
        for end in range(start,n):
            
            substring= string[start:end+1]
            
            if check(substring):
                
                length =  end-start+1
                
                if length > max_len:
                    
                    max_len =  length
                    
                    new= substring
                    
    return new 

s="abbacaa"

print(main(s))

