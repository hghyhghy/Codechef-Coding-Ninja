


#valid parenthesis

def main(string):
    
    result=[]
    matching = {')': '(', ']': '[', '}': '{'}

    for char in string:
        
        if char in matching.values():
            
            result.append(char)

        
        elif char in matching:
            
            if not result:
                
                return False
            
            top=result.pop()

            if  matching[char] != top:
                
                return False
            
    
    return len(result) == 0

S1 = "{[()()]}"
print(main(S1))