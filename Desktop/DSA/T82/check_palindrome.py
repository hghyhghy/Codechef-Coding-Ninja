# Problem statement
# Ninja’s friend challenged him with a trick question. He gave him a string ‘S’ and asked him if it is possible to make this string palindrome by deleting one character from the string. Can you help the ninja to solve this problem?

# You are given a string ‘S’ of size ‘N’.You have to determine whether it is possible to make the string palindrome by deleting at most one character.

# For Example
# If the string is ‘AZBCDCBA’, the answer will be YES as we can delete the character ‘Z’ and the remaining string is a palindrome. 

def is_palindrome(string:str)->bool:
    
    return string.lower() == string[::-1].lower()

def main(string:str)->bool:
    
    n=len(string)
    
    for i in range(n):
        
        new_string =string[:i]+string[i+1:]
        
        if is_palindrome(new_string):
            
            return True
        
    
    return False

s = "abca"
print(main(s))