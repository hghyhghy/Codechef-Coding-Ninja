# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def valid_palindrome(string):
    
    normalized_char="".join(char.lower() for char in string if char.isalnum())
    
    n=len(normalized_char)
    left=0
    right=n-1
    
    while left <= right:
        
        if normalized_char[left] != normalized_char[right]:
            
            return False
          
    
        return True
 
s1 = "A man, a plan, a canal: Panama"
print(valid_palindrome(s1))