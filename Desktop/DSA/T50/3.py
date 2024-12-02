# Problem statement
# You have been given a string 'S' containing only three types of characters, i.e. '(', ')' and '*'.

# A Valid String is defined as follows:

# 1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# 5. An empty string is also valid.
# Your task is to find out whether the given string is a Valid String or not.

def valid_parenthesis(string:str) -> bool:
    
    low=0
    high= 0

    for char in string:
        
        if char == "(":
            
            low  += 1
            high += 1
        
        elif char == ")":
            
            low -= 1
            high -=1 
            
        elif char == "*":
            
            low -=1 
            high += 1
            
        
        if low <0:
            
            low= 0
            
        if high < 0:
            
            return False
    
    return low == 0

print(valid_parenthesis(")("))           # Output: True

    
    