#check palindrome by deleting one char 

def check(string:str)->bool:
    
    return string.lower() == string[::-1].lower()

def main(string:str)->bool:
    
    n=len(string)

    for i in range(n):
        
        new_str= string[:i]+string[i+1:]

        if  check(new_str):
            
            return True
        
    
    return False

i=list(map(str,input("enter string").split()))

for string in i:
    
    if main(string):
        
        print(f"Yes, the string '{string}' can be made a palindrome by removing one character.")

    else:
        
        print(f"No, the string '{string}' cannot be made a palindrome by removing one character.")