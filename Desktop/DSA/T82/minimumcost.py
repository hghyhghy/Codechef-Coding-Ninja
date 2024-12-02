# Problem statement
# Ninja has been given a string ‘STR’ containing either ‘{’ or ‘}’. 'STR’ is called valid if all the brackets are balanced. Formally for each opening bracket, there must be a closing bracket right to it.

# For Example:
# “{}{}”, “{{}}”, “{{}{}}” are valid strings while “}{}”, “{}}{{}”, “{{}}}{“ are not valid strings.
# Ninja wants to make ‘STR’ valid by performing some operations on it. In one operation, he can convert ‘{’ into ‘}’ or vice versa, and the cost of one such operation is 1.

# Your task is to help Ninja determine the minimum cost to make ‘STR’ valid.

# For Example:
# Minimum operations to make ‘STR’ =  “{{“ valid is 1.
# # In one operation, we can convert ‘{’ at index ‘1’ (0-based indexing) to ‘}’. The ‘STR’ now becomes "{}" which is a valid string.

def minimum_cost_valid_string(string:str)->int:
    
    if len(string) % 2 != 0:
        
        return -1
    
    stack=[]
    
    for char in string:
        
        if char == "{":
            
            stack.append(char)
            
        else:
            
            if stack and stack[-1]== "{":
                
                stack.pop()
                
            else:
                
                stack.append(char)
                
    
    open_bracket=close_bracket=0

    
    while stack:
        
        if stack.pop() == "{":
            
            open_bracket += 1
            
        else:
            
            close_bracket += 1
            
    
    return (open_bracket+1)//2 + (close_bracket+1)//2

STR = "{{{{}}"
print(minimum_cost_valid_string(STR))
            
            