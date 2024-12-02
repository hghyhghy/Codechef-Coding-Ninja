# Problem statement
# You're given an alphabetical string ‘S’.



# Determine whether it is palindrome or not. A palindrome is a string that is equal to itself upon reversing it

def checking_palindrome(string):
    
    n=len(string)
    left = 0
    right = n-1
    
    if  n ==1 :
        
        return None
    
    while left < right:
        
        if  string[left] != string[right]:
            
            return False
        
        left += 1
        right -= 1
        
        
    return  True

a="racecar"
print(checking_palindrome(a))