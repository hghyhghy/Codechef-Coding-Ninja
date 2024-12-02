
#remove consecutive duplicates 

def main(string):
    
    if not string:
        
        return None
    
    n=len(string)
    dp=""

    for i in  range(n):
        
        if string[i]  != string[i-1]:
            
            dp += string[i]

    return dp

s = "aabbccddeeff"
print(main(s))