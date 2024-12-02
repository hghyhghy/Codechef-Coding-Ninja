
#valid palindrome

def main(string:str)->bool:
    
    n=len(string)
    left=0
    right=n-1
    
    while left < right:
        
        if string[left] !=string[right]:
            
            return False
        
        left +=1
        right-=1
        
    return True

string=input("enter string")
print(main(string))