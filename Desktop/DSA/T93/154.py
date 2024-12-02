
#remove duplicate char from the string 

def  main(string):
    
    seen=set()
    result=""

    for char in string:
        
        if char in seen:
            
            continue
        
        seen.add(char)
        result += char
        
    return  result

a="abracadabra"
print(main(a))