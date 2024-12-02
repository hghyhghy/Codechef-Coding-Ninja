# Problem statement
# You are given a string ('STR') of length 'N'. Find the longest palindromic substring. If there is more than one palindromic substring with the maximum length, return the one with the smaller start index.

# Note:
# A substring is a contiguous segment of a string.
# For example : The longest palindromic substring of "ababc" is "aba", since "aba" is a palindrome and it is the longest substring of length 3 which is a palindrome, there is another palindromic substring of length 3 is "bab" since "aba" starting index is less than "bab", so "aba" is the answer.

def check_palin(string:str)->bool:
    
    return string.lower() == string[::-1].lower()

def main(string:str)->str:
    
    n=len(string)
    max_len = 0
    palindrome = ""
    
    for i in range(n):
        
        for j in range(i,n):
            
            substring=string[i:j+1]
            
            
            if check_palin(substring):
                
                if len(substring) > max_len:
                    
                    max_len =  len(substring)
                    
                    palindrome = substring
                    
    return palindrome

s = "ababc"
print(main(s))