
def main(string):
    
    brackets="()[]{}"
    
    for bracket in brackets:
        
        string=string.replace(bracket,"")

    
    return string

print(main("(a+b) - (c-d)"))
