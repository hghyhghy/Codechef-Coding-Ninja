# The function accepts a string ‘str’ as its argument. The function needs to determine whether the string is a palindrome or not. A palindrome is a word or phrase that reads the same backward as forward.

def ispalindrome(string):
    
    right=len(string)-1
    left=0
    
    while left < right:
        
        if string[left] == string[right]:
            
            return True
        
        left += 1
        right -= 1
        
        
str= "madam"
print(ispalindrome(str))