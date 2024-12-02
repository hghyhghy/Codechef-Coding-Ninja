
#palindrome 
def main(string:str)->bool:
    
    string=[char .lower() for char in string if char.isalnum()]
    n=len(string)
    left=0
    right=n-1
    
    while left < right:
        
        if string[left] != string[right]:
            
            return False
        
        left +=1 
        right -=1
        
    
    return True

s = "A man, a plan, a canal, Panama"
print(main(s))