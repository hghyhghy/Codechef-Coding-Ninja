# You are given a string 'S'. Your task is to check whether the string is palindrome or not. For checking palindrome, consider alphabets and numbers only and ignore the symbols and whitespaces.

def check_palindrome(array):
    
    n=len(array)
    left=0
    right=n-1
    
    while left < right:
        
        if array[left] != array[right]:
            
            return False
        
        left += 1
        right -=1
        
    return True

s="abba"
print(check_palindrome(s))