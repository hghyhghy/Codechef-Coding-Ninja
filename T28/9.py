# Problem statement
# You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .



# Return true if the given string 'S' is balanced, else return false.

def valid_parenthesis(string):
    
    pairs = {')': '(', '}': '{', ']': '['}
    stack=[]

    for char in string:
        
        if char in pairs.values():
            
            stack.append(char)

        elif char in pairs.keys():
            
            if not stack or stack[-1] != pairs[char]:
                
                return False
            
            stack.pop()

    
    return not stack

s = "{[()()]}"
print(valid_parenthesis(s))