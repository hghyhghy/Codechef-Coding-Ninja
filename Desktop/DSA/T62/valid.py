# Problem statement
# You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .



# Return true if the given string 'S' is balanced, else return false.



# For example:
# 'S' = "{}()".

# There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
# So the 'S' is Balanced.

def valid_parenthesis(string):
    
    stack=[]
    matching = {')': '(', ']': '[', '}': '{'}

    for char in string:
        
        if char in matching.values():
            
            stack.append(char)

        
        elif char in matching:
            
            if not stack:
                
                return False
            
            top=stack.pop()

            if  matching[char] !=  top:
                
                return False
            
            
    return len(stack) == 0 


S1 = "{[()()]}"
print(valid_parenthesis(S1))