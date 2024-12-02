# 19 upvotes
# Asked in companies
# Problem statement
# Given a string, determine if it is a palindrome, considering only alphanumeric characters.

# Palindrome
# A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.
# Example:
# If the input string happens to be, "malayalam" then as we see that this word can be read the same as forward and backwards, it is said to be a valid palindrome.

# The expected output for this example will print, 'true'.
# # From that being said, you are required to return a boolean value from the function that has been asked to implement.


def ispalindrome(string:str)->bool:
    
    n=len(string)
    left=0
    right=n-1
    
    while left<right:

        while left < right and  not string[left].isalnum():
            
            left +=1
            
        while left < right and not string[right].isalnum():
            
            right -= 1
            
            
        if string[left].lower()  != string[right].lower():
            
            return False
        
        left +=1
        
        right -=1
        
    return True

print(ispalindrome("ab"))
        
        