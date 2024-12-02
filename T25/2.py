# Remove brackets from an algebraic expression

def remove_bracket(string):
    
    brackets="()[]{}"

    for braket in brackets:
        
        string=string.replace(braket,"")
        
    return string


print(remove_bracket("(a+b) - (c-d)"))