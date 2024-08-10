# valid parenthesis checker brute force approach 

def valid_parenthesis_checker(s:str) -> bool:
    
    while '()' in s or '{}' in s or '[]' in s:
        
        s=s.replace('()',"").replace('{}',"").replace('[]',"")
        
    return len(s) == 0

print(valid_parenthesis_checker("(]"))    