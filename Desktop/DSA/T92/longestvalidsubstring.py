# Problem statement
# You are given a string 'STR' consisting only of opening and closing parenthesis i.e. '(' and ')', your task is to find out the length of the longest valid parentheses substring.

# Note:
# The length of the smallest valid substring '()' is 2.
# For example:
# 'STR' = “()()())” here we can see that except the last parentheses all the brackets are making a valid parenthesis. Therefore, the answer for this will be 6.

def check(string:str)->bool:
    
    r=[]
    
    for char in string:
        
        if char == "(":
            
            r.append(char)

        elif char == ")":
            
            if not r:
                
                return False
            
            r.pop()
            
        
    return len(r) == 0

def main_function(string:str)->int:
    
    n=len(string)
    maximum = float("-inf")

    for i in range(n):
        
        for j in range(i+2,n+1, 2):
            
            if check(string[i:j]):
                
                maximum = max(maximum,j-i)
                
    
    return maximum

s = "()()())"
print(main_function(s))