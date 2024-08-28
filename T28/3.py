# You are given a string 'S'. Your task is to check whether the string is palindrome or not. For checking palindrome, consider alphabets and numbers only and ignore the symbols and whitespaces.

# Note :

# String 'S' is NOT case sensitive.

def is_palindrome_string(string):
    
    string=[char.lower() for char in string if char.isalnum()]
    
    left=0
    right =len(string) -1
    
    while left < right:
        
        if string[left] != string[right]:
            
            return False
        
        left += 1
        
        right -=1
        
    
    return True

s = "A man, a plan, a canal, Panama"
print(is_palindrome_string(s))