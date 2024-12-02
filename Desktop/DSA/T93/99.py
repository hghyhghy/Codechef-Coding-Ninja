

#prefix sum

def main(strings:str)->str:

    if not strings:
        
        return None
    
    prefix =strings[0]

    for  string in strings:
        
        while not string.startswith(prefix):
            
            prefix=prefix[:-1]

            if not prefix:
                
                return " "

    return prefix

arr=list(map(str,input().split()))
print(main(arr))    
    