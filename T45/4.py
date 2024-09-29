# Problem statement
# You are given a string ('STR') of length 'N'. Find the longest palindromic substring. If there is more than one palindromic substring with the maximum length, return the one with the smaller start index.

# Note:
# A substring is a contiguous segment of a string.
# For example : The longest palindromic substring of "ababc" is "aba", since "aba" is a palindrome and it is the longest substring of length 3 which is a palindrome, there is another palindromic substring of length 3 is "bab" since "aba" starting index is less than "bab", so "aba" is the answer.

def is_palindrome(string):

    return string == string[::-1]

def main(string):
    
    n=len(string)
    max_lenght=0
    palindrome=[]

    for start in range(n):
        for end in range(start,n):
            
            substring=string[start:end+1]
            if is_palindrome(substring):
                
                length = end-start+1
                if length > max_lenght:
                    
                    max_lenght = length
                    palindrome = substring
                    
    return palindrome

arr = [1, 2, 3, 2, 1, 4, 5, 4, 2, 1]
print(main(arr))
    
    