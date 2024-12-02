# Problem statement
# You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .



# Return true if the given string 'S' is balanced, else return false.



# For example:
# 'S' = "{}()".

# There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
# So the 'S' is Balanced.

def valid_parenthesis(array):
    
    stack=[]
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in array:
        
        if char in matching_brackets.values():
            
            stack.append(char)

        elif char in matching_brackets:
            
            if stack and stack[-1] ==  matching_brackets[char]:
                
                stack.pop()

            else:
                
                return False
            
    return len(stack ) == 0


print(valid_parenthesis("{[()]}"))
     