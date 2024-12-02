# Problem statement
# You are given a string 'STR' consisting of lower and upper case characters. You need to remove the consecutive duplicates characters, and return the new string.



# Note :
# You don't have to print anything, it has already been taken care of. Just implement the given function.

def remove_consecutive_suplicate(string:str)->str:
    
    n=len(string)
    
    result=string[0]
    
    for i in range(1,n):
        
        if string[i] != string[i-1]:
            
            result += string[i]
            
    return "".join(result)

STR = "aabbccddeeeffggh"
print(remove_consecutive_suplicate(STR))      