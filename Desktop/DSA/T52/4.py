# Problem statement
# Given a string, determine if it is a palindrome, considering only alphanumeric characters.

# Palindrome
# A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.
# Example:
# If the input string happens to be, "malayalam" then as we see that this word can be read the same as forward and backwards, it is said to be a valid palindrome.

# The expected output for this example will print, 'true'.
# From that being said, you are required to return a boolean value from the function that has been asked to implement.

def string_palindrome(string):
    
    n=len(string)

    left=0
    right=n-1
    
    while left < right:
        
        if string[left] != string[right]:
            
            return False
        
        left += 1
        right -= 1
        
    return True

a="abcdcba"
print(string_palindrome(a))