

#valid parenthesis

def main(string):
    
    pairs = {')': '(', '}': '{', ']': '['}
    store=[]

    for char in string:
        
        if char in pairs.values():
            
            store.append(char)

        elif char in pairs.keys():
            
            if not store or store[-1] != pairs[char]:
                
                return False
            
            store.pop()

    
    return not store
s = "{[()()]}"
print(main(s))