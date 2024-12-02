# You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .



# Return true if the given string 'S' is balanced, else return false.



# For example:
# 'S' = "{}()".

# There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
# So the 'S' is Balanced.

def valid_parenthesis(string:str)->bool:
    
    matching_braces = {')': '(', '}': '{', ']': '['}
    stack=[]
    
    for char in string:
        
        if char in matching_braces.values():
            
            stack.append(char)
            
        elif char in matching_braces:
            
            if not stack or stack.pop() != matching_braces[char]:
                
                return False
            
    return len(stack) == 0

S = "{}()"
print(valid_parenthesis(S))
