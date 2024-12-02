# Problem statement
# Given a string ’S’ consisting of lower case English letters, you are supposed to return the longest palindromic substring of ‘S’.

# Note that in case of more than one longest palindromic substrings with the same length you need to return the rightmost substring in the given string. For example in string “bbbab”, there are two possible longest palindromic substrings i.e. “bbb” and “bab”, and since you are supposed to return the rightmost substring, so you need to return “bab” as the answer.

# Note:
# A substring is a contiguous sequence of elements within a string (for example, “bcd” is a substring of “abcde” while “bce” is not).

# A string is said to be palindrome if the reverse of the string is the same as the actual string. For example, “abba” is a palindrome, but “abbc” is not a palindrome.

def pal(string:str)->bool:
    
    return string.lower() == string[::-1].lower()

def longest_palindroix_substring(string:str)->str:
    
    n=len(string)
    max_len=float("-inf")
    longest = ""

    for i in range(n):
        
        for j in range(i,n):
            
            substring = string[i:j+1]
            
            if pal(substring):
                
                length= j-i+1
                
                if length > max_len or (length==max_len and i > string.index(longest)):
                    
                    max_len = length
                    longest=substring
                    
    return longest

a="bbbab"
print(longest_palindroix_substring(a))