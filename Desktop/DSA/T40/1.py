# You're given an alphabetical string ‘S’.



# Determine whether it is palindrome or not. A palindrome is a string that is equal to itself upon reversing it.

def checking_palindrome(string):
    
    n=len(string)
    left=0
    right=n-1
    
    
    while left < right:
        
        if string[left] != string[right]:
            
            return False
        
        left  += 1
        right -=1 
        
    
    return  True

S = "madam"
print(checking_palindrome(S))