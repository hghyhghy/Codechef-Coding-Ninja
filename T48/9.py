# You are given a string 'str' of length 'N'.



# Your task is to return the longest palindromic substring. If there are multiple strings, return any.



# A substring is a contiguous segment of a string.

def is_palindrome(string):
    
    return string == string[::-1]

def main(string):
    
    n=len(string)
    if not string or n==1:
        
        return None
    
    max_lenght = 0
    largest=""

    for start in range(n):
        
        for end in range(start,n):
            
            substring = string[start:end+1]
            
            if is_palindrome(substring):
                
                lenght = end-start+1
                if lenght > max_lenght:
                    
                    max_lenght = lenght
                    largest =substring
                    
    return max_lenght,largest

s = "babad"
print(main(s))
                    
                    